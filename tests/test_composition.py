"""Real Foundation composition; no provider calls in ordinary tests."""
from pathlib import Path

import pytest

import amplifier_foundation as foundation
ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.asyncio
async def test_root_loads_from_an_unrelated_workspace(tmp_path, monkeypatch):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / "bundle.md"), strict=True)
    plan = bundle.to_mount_plan()
    assert plan["session"]["context"]["config"]["engine"] == "boundary"
    assert {tool["module"] for tool in bundle.tools} >= {"tool-delegate", "tool-transcript", "tool-bash", "tool-apply-patch"}
    patch = next(tool for tool in bundle.tools if tool["module"] == "tool-apply-patch")
    assert '@main#' in patch['source']
    assert patch['config'] == {'engine': 'native'}
    assert not bundle.providers
    assert "agent: self" in bundle.instruction
    assert plan['session']['orchestrator']['config']['programmatic_dispatch'] is True
    bash = next(tool for tool in bundle.tools if tool['module'] == 'tool-bash')
    assert bash['config']['managed_processes'] is True
    assert bash['config']['managed_stdin'] is True
    assert {'tool-exec', 'tool-web'} <= {tool['module'] for tool in bundle.tools}
    web = next(tool for tool in bundle.tools if tool['module'] == 'tool-web')
    assert web['config']['search_engine'] == 'ddgs'


@pytest.mark.asyncio
async def test_overlay_preserves_provider_and_unrelated_tools(tmp_path, monkeypatch):
    monkeypatch.setenv("AMPLIFIER_HOME", str(tmp_path / "shared"))
    base = foundation.Bundle(name="configured", providers=[{"module": "provider-test", "config": {"default_model": "chosen"}}],
                             tools=[{"module": "tool-extra"}], session={"context": {"module": "context-simple"}})
    overlay = await foundation.load_bundle(str(ROOT / "behaviors/work-local.yaml"), strict=True)
    result = base.compose(overlay)
    assert result.providers == base.providers
    assert result.session["context"]["module"] == "context-managed"
    assert {tool["module"] for tool in result.tools} == {"tool-extra", "tool-transcript"}
    assert result.session["orchestrator"]["config"]["background_delegate"] is False


@pytest.mark.asyncio
async def test_anchors_work_preserves_anchors_capabilities(tmp_path, monkeypatch):
    monkeypatch.setenv('AMPLIFIER_HOME', str(tmp_path / 'shared'))
    monkeypatch.chdir(tmp_path)
    bundle = await foundation.load_bundle(str(ROOT / 'presets/anchors-work.md'), strict=True)
    assert bundle.session['context']['module'] == 'context-managed'
    assert bundle.session['orchestrator']['module'] == 'loop-live'
    assert bundle.session['orchestrator']['config']['background_delegate'] is False
    assert bundle.session['orchestrator']['config']['programmatic_dispatch'] is True
    assert next(row for row in bundle.tools if row['module'] == 'tool-web')['config']['search_engine'] == 'ddgs'
    assert {row['module'] for row in bundle.tools} >= {'tool-web', 'tool-todo', 'tool-delegate', 'tool-transcript', 'tool-skills'}
    assert bundle.agents
    assert '@anchors:context/system.md' in bundle.instruction
    assert not bundle.providers
