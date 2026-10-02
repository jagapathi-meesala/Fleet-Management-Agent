from pathlib import Path

def test_required_headings():
    t = Path('EXPLAINABILITY.md').read_text()
    required = ['## Inputs and Data Sources', '## Decision and Reasoning', '## Limits and Constraints']
    assert all(t.count(h) == 1 for h in required)
    assert '## Inputs\n' not in t
    assert '## Decision\n' not in t
    assert '## Limits\n' not in t

def test_skills_exist():
    for s in ['fleet-monitoring', 'maintenance-planning', 'fleet-analytics']:
        assert Path(f'skills/{s}/SKILL.md').is_file()
