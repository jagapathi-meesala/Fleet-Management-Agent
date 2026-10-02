from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

def load_tools(registry):
    for path in Path(__file__).parent.glob("*.py"):
        if path.name == "__init__.py": continue
        spec=spec_from_file_location(path.stem.replace("-","_"), path)
        mod=module_from_spec(spec); spec.loader.exec_module(mod); registry.register(mod.tool)
    return registry
