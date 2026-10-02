from pathlib import Path
import re
import yaml


def test_manifest_schema_shape():
    m = yaml.safe_load(Path('agent.yaml').read_text())
    assert isinstance(m, dict)
    assert set(m) <= {
        'spec_version','name','version','description','author','license','model',
        'extends','dependencies','skills','tools','agents','delegation','runtime',
        'a2a','compliance','registries','tags','mcp_servers','metadata'
    }
    assert m['spec_version'] == '0.1.0'
    assert re.fullmatch(r'^[a-z][a-z0-9-]*$', m['name'])
    assert re.fullmatch(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$', str(m['version']))
    assert isinstance(m['description'], str) and m['description']
    assert all(re.fullmatch(r'^[a-z][a-z0-9-]*$', x) for x in m['skills'])
    assert all(re.fullmatch(r'^[a-z][a-z0-9-]*$', x) for x in m['tools'])
