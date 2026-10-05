"""Work plus amp-dev preserves Work, not an Anchors-derived host."""
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

from amplifier_foundation import Bundle, load_bundle
from amplifier_foundation.bundle._prepared import PreparedBundle, BundleModuleResolver
from amplifier_foundation.mentions import BaseMentionResolver
from amplifier_foundation.modules.activator import ModuleActivator

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.asyncio
async def test_work_amp_dev_preserves_work_and_resolves_portable_expert(tmp_path, monkeypatch):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    base = await load_bundle(str(ROOT / "bundle.md"), strict=True)
    dev = await load_bundle(str(ROOT / "bundles/work-amp-dev.md"), strict=True)
    assert dev.session == base.session
    assert dev.providers == base.providers == []
    assert dev.hooks == base.hooks
    assert dev.instruction == base.instruction == "@work:context/system.md"
    assert dev.session["orchestrator"]["module"] == "loop-live"
    assert dev.session["context"]["module"] == "context-managed"
    assert not any(name.startswith("anchors:") for name in dev.agents)
    assert set(dev.agents) == {"amp-dev:amplifier-dev-expert",
        "amplifier-tester:setup-digital-twin", "amplifier-tester:validator",
        "digital-twin-universe:dtu-profile-builder"}
    prepared = PreparedBundle({}, BundleModuleResolver(module_paths={}), dev)
    resources = BaseMentionResolver(bundles=prepared._build_bundles_for_resolver(dev))
    assert resources.resolve("@work:context/system.md") == ROOT / "context/system.md"
    expert = resources.resolve("@amp-dev:agents/amplifier-dev-expert.md")
    assert expert is not None and expert.is_file()
    assert resources.resolve("@foundation:context/amplifier-dev/ecosystem-map.md").is_file()
    assert "@anchors:" not in expert.read_text()
    skills = next(row for row in dev.tools if row["module"] == "tool-skills")["config"]["skills"]
    assert skills[:5] == [".amplifier/skills", ".agents/skills",
        "~/.amplifier/skills", "~/.agents/skills", "@work-skills:skills"]
    overridden = dev.compose(Bundle(name="app", session={
        "orchestrator": {"module": "app-loop"},
        "context": {"module": "app-context"}},
        providers=[{"module": "provider-test", "config": {"default_model": "chosen"}}]))
    assert overridden.session["orchestrator"]["module"] == "app-loop"
    assert overridden.session["context"]["module"] == "app-context"
    assert overridden.providers[0]["config"]["default_model"] == "chosen"


@pytest.mark.asyncio
async def test_actual_root_and_delegated_prompts_preserve_instruction_once(tmp_path, monkeypatch):
    """Exercise production prompt construction; module activation/model calls are separate DTU checks."""
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    (tmp_path / "AGENTS.md").write_text("host conventions sentinel")
    bundle = await load_bundle(str(ROOT / "bundles/work-amp-dev.md"), strict=True)
    bundle.load_agent_metadata()
    monkeypatch.setattr(ModuleActivator, "activate_all", AsyncMock(return_value={}))
    monkeypatch.setattr(ModuleActivator, "finalize", lambda self: None)
    prepared = await bundle.prepare(install_deps=False)
    # create_session resolves these after initialize, before registering its factory.
    prepared.bundle.resolve_pending_context()
    session = MagicMock()
    session.coordinator.hooks.emit = AsyncMock()
    prompt = await prepared.create_system_prompt_factory(session, session_cwd=tmp_path)()
    assert prompt.count((ROOT / "context/system.md").read_text().strip()) == 1
    assert prompt.count("# Amplifier Ecosystem") == 1
    assert "Principles governing every action" not in prompt
    expert = prepared.mount_plan["agents"]["amp-dev:amplifier-dev-expert"]
    child = bundle.compose(Bundle(name="amp-dev:amplifier-dev-expert",
                                  instruction=expert["instruction"]))
    child_prepared = await child.prepare(install_deps=False)
    child_prepared.bundle.resolve_pending_context()
    child_prompt = await child_prepared.create_system_prompt_factory(session, session_cwd=tmp_path)()
    assert "# Amplifier Ecosystem Map" in child_prompt
    assert "# Amplifier Development Workflows" in child_prompt
    assert "# Amplifier Testing Patterns" in child_prompt
    assert child_prompt.count("# Agent Baseline") == 1
    assert (ROOT / "context/system.md").read_text().strip() not in child_prompt
    assert "host conventions sentinel" not in child_prompt