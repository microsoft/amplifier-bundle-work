"""Real Foundation composition and skill loading, without provider calls."""
from contextlib import asynccontextmanager
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
import re

import amplifier_foundation as foundation
from amplifier_core import AmplifierSession
from amplifier_foundation.mentions import BaseMentionResolver
from amplifier_module_tool_skills import mount
from amplifier_module_tool_skills.discovery import discover_skills
import pytest


ROOT = Path(__file__).resolve().parents[1]
SKILL_SOURCE = "@work-skills:skills"
IMAGE_SKILL_SOURCE = "@imagegen:skills"
TOOL_SOURCE = (
    "git+https://github.com/microsoft/amplifier-bundle-skills@"
    "main#subdirectory=modules/tool-skills"
)


@pytest.mark.asyncio
async def test_extension_creator_example_has_loadable_module_and_namespace(tmp_path, monkeypatch):
    """The documented default must not put a source URL in the module-ID field."""
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    instructions = (ROOT / "skills/plugin-creator/SKILL.md").read_text()
    example = re.search(r"```yaml\n(.*?)\n```", instructions, re.DOTALL)
    assert example
    extension = tmp_path / "extension"
    skill = extension / "skills/example"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: example\ndescription: Synthetic example.\n---\nUse the supplied facts.\n")
    (extension / "bundle.md").write_text(example.group(1))
    bundle = await foundation.load_bundle(str(extension / "bundle.md"), strict=True)
    bundle.resolve_pending_context()
    plan = bundle.to_mount_plan()
    module = next(row for row in plan["tools"] if row["module"] == "tool-skills")
    assert module["source"] == TOOL_SOURCE
    assert module["config"]["skills"] == ["@example-skills:skills"]
    assert bundle.base_path == extension
    resolver = BaseMentionResolver(bundles={bundle.name: bundle}, base_path=tmp_path)
    assert resolver.resolve("@example-skills:skills") == extension / "skills"


def skill_module(bundle):
    return next(row for row in bundle.tools if row["module"] == "tool-skills")


def expected_skills(bundle):
    local = discover_skills(ROOT / "skills")
    image_root = bundle.source_base_paths["imagegen"] / "skills"
    images = discover_skills(image_root)
    assert len(local) == 32
    assert set(images) == {"imagegen"}
    assert not set(local) & set(images), "Canonical skills must not be shadowed by Work copies."
    return {**local, **images}


@asynccontextmanager
async def mounted_skills(bundle, tmp_path, *, visibility=True, eager_resolver=False):
    """Use the real kernel and resolver, with synthetic user-level skill files."""
    config = deepcopy(skill_module(bundle)["config"])
    user_sources = {
        "~/.amplifier/skills": str(tmp_path / "user-skills"),
        "~/.agents/skills": str(tmp_path / "user-shared-skills"),
    }
    config["skills"] = [user_sources.get(source, source) for source in config["skills"]]
    config["visibility"]["enabled"] = visibility
    session = AmplifierSession(bundle.to_mount_plan())
    coordinator = session.coordinator
    # Preserve every namespace's own source root, as PreparedBundle does.
    # Current Foundation registers before mount; older hosts register later.
    bundles = {
        namespace: replace(bundle, base_path=path)
        for namespace, path in bundle.source_base_paths.items()
    }
    resolver = BaseMentionResolver(bundles=bundles, base_path=tmp_path)
    if eager_resolver:
        coordinator.register_capability("mention_resolver", resolver)
    cleanup = await mount(coordinator, config)
    tool = coordinator.get("tools")["load_skill"]
    try:
        yield coordinator, tool, resolver
    finally:
        if cleanup:
            await cleanup()


@pytest.mark.asyncio
@pytest.mark.parametrize("manifest", ["bundle.md", "presets/anchors-work.md"])
async def test_work_roots_compose_skill_namespace_from_unrelated_workspace(
    manifest, tmp_path, monkeypatch
):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / manifest), strict=True)
    module = skill_module(bundle)
    assert module["source"] == TOOL_SOURCE
    assert SKILL_SOURCE in module["config"]["skills"]
    assert module["config"]["skills"][-2:] == [SKILL_SOURCE, IMAGE_SKILL_SOURCE]
    assert bundle.source_base_paths["work-skills"] == ROOT
    assert not bundle.providers
    assert bundle.session["orchestrator"]["config"]["background_delegate"] is False
    bundle.resolve_pending_context()
    assert ROOT / "context/work-skills.md" in bundle.context.values()


@pytest.mark.asyncio
async def test_skill_behavior_preserves_existing_runtime_provider_and_sources(
    tmp_path, monkeypatch
):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    original = foundation.Bundle(
        name="configured",
        providers=[{"module": "provider-existing", "config": {"default_model": "chosen"}}],
        tools=[{"module": "tool-extra"}, {
            "module": "tool-skills", "config": {"skills": ["@existing:skills"]}
        }],
        session={"orchestrator": {"module": "existing-loop"},
                 "context": {"module": "existing-context"}},
        agents={"existing": {"description": "Existing specialist"}},
        instruction="Existing operating policy.",
    )
    behavior = await foundation.load_bundle(str(ROOT / "behaviors/work-skills.yaml"), strict=True)
    result = original.compose(behavior)
    assert result.providers == original.providers
    assert result.session == original.session
    assert result.agents == original.agents
    assert result.instruction == original.instruction
    assert {row["module"] for row in result.tools} == {"tool-extra", "tool-skills"}
    assert skill_module(result)["config"]["skills"] == [
        "@existing:skills", ".amplifier/skills", ".agents/skills",
        "~/.amplifier/skills", "~/.agents/skills", SKILL_SOURCE, IMAGE_SKILL_SOURCE
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize("visibility,eager_resolver", [(True, True), (True, False), (False, False)])
@pytest.mark.parametrize("manifest", ["bundle.md", "behaviors/work-skills.yaml", "presets/work-images.md"])
async def test_real_loader_discovers_and_loads_every_shipped_skill(
    tmp_path, monkeypatch, visibility, eager_resolver, manifest
):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / manifest), strict=True)
    if manifest == "behaviors/work-skills.yaml":
        # A behavior deliberately leaves the host's session implementation alone.
        # The real kernel still requires those IDs even when only skills mount.
        host = foundation.Bundle(name="skill-test-host", session={
            "orchestrator": {"module": "test-loop"},
            "context": {"module": "test-context"},
        })
        bundle = host.compose(bundle)
    expected = expected_skills(bundle)
    skill_files = set((ROOT / "skills").glob("*/SKILL.md"))
    skill_files |= set((bundle.source_base_paths["imagegen"] / "skills").glob("*/SKILL.md"))
    assert len(expected) == 33, "The complete port must be discoverable, not just present on disk."
    assert {row.path for row in expected.values()} == skill_files
    async with mounted_skills(
        bundle, tmp_path, visibility=visibility, eager_resolver=eager_resolver
    ) as (coordinator, tool, resolver):
        assert set(tool.skills) == (set(expected) if eager_resolver else set())
        assert resolver.resolve(SKILL_SOURCE) == ROOT / "skills"
        assert resolver.resolve(IMAGE_SKILL_SOURCE) == bundle.source_base_paths["imagegen"] / "skills"
        if not eager_resolver:
            coordinator.register_capability("mention_resolver", resolver)
        request = await coordinator.hooks.emit("provider:request", {})
        discovery = coordinator.get_capability("skills_discovery")
        assert {name for name, _ in discovery.list_skills()} == set(expected)
        if visibility:
            catalog = request.context_injection or ""
            assert all(name in catalog for name in expected)
        listing = await tool.execute({"list": True})
        assert listing.success
        for name, metadata in expected.items():
            assert metadata.context != "fork", "Portable guidance must not start workers on load."
            result = await tool.execute({"skill_name": name})
            assert result.success, (name, result.error)
            assert result.output["skill_name"] == name
            assert Path(result.output["skill_directory"]) == metadata.path.parent
            assert len(result.output["content"].strip()) > len(name) + 4
        # A second request must preserve the same catalog and avoid duplicate paths.
        await coordinator.hooks.emit("provider:request", {})
        assert tool.skills_dirs.count(ROOT / "skills") == 1
        assert tool.skills_dirs.count(bundle.source_base_paths["imagegen"] / "skills") == 1


@pytest.mark.asyncio
@pytest.mark.parametrize("first_scope", range(4))
@pytest.mark.parametrize("name", ["imagegen", "artifact-template-analytics-dashboard"])
async def test_project_native_and_shared_scopes_precede_user_and_library(
    tmp_path, monkeypatch, first_scope, name
):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / "bundle.md"), strict=True)
    expected = expected_skills(bundle)
    assert name in expected
    scopes = [
        (tmp_path / ".amplifier/skills", "Workspace-specific guidance."),
        (tmp_path / ".agents/skills", "Shared workspace guidance."),
        (tmp_path / "user-skills", "User-specific guidance."),
        (tmp_path / "user-shared-skills", "Shared user guidance."),
    ]
    for source, text in scopes[first_scope:]:
        folder = source / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Override for testing.\n---\n\n{text}\n"
        )
    async with mounted_skills(bundle, tmp_path) as (coordinator, tool, resolver):
        coordinator.register_capability("mention_resolver", resolver)
        await coordinator.hooks.emit("provider:request", {})
        result = await tool.execute({"skill_name": name})
        assert result.success
        assert scopes[first_scope][1] in result.output["content"]
        assert Path(result.output["skill_directory"]) == scopes[first_scope][0] / name
        assert set(tool.skills) == set(expected)
