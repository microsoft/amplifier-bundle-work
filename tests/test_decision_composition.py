from pathlib import Path
import pytest
import amplifier_foundation as foundation

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.asyncio
@pytest.mark.parametrize('root', ['bundle.md', 'bundles/work-amp-dev.md'])
async def test_decisions_are_optional_for_both_work_roots(root, tmp_path, monkeypatch):
    monkeypatch.setenv('AMPLIFIER_HOME', str(tmp_path / 'shared'))
    monkeypatch.chdir(tmp_path)
    work = await foundation.load_bundle(str(ROOT / root), strict=True)
    assert [row['module'] for row in work.tools].count('tool-ui-use') == 1
    assert 'hooks-decision-models' not in {row['module'] for row in work.hooks}
    prior_session, prior_providers = work.session, work.providers
    for name in ('work-ui-use',):
        work = work.compose(await foundation.load_bundle(str(ROOT / 'behaviors' / (name+'.yaml')), strict=True))
    assert work.session == prior_session and work.providers == prior_providers
    ui = next(row for row in work.tools if row['module'] == 'tool-ui-use')
    assert ui['config']['selection'] == {'browser': {'mode': 'standard'}, 'computer': {'mode': 'standard'}}
    assert ui['config']['programmatic_dispatch'] is True
    assert 'hooks-decision-models' not in {row['module'] for row in work.hooks}
    assert 'tool-computer-use' not in {row['module'] for row in work.tools}
    # Desktop execution is a separate opt-in, not an implicit Work dependency.
    ui_source = Path(work.source_base_paths['ui-use-behavior'])
    computer_behavior = ui_source / 'computer.yaml'
    if not computer_behavior.is_file():
        computer_behavior = ui_source / 'behaviors/computer.yaml'
    desktop = work.compose(await foundation.load_bundle(str(computer_behavior), strict=True))
    assert desktop.session == prior_session and desktop.providers == prior_providers
    assert next(row for row in desktop.tools if row['module'] == 'tool-computer-use')['config']['observed_control'] is True
