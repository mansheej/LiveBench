import sys
import types


class RuntimeModule:
    @classmethod
    def from_string(cls, name: str, doc: str, code: str) -> types.ModuleType:
        module = types.ModuleType(name, doc)
        sys.modules[name] = module
        exec(code, module.__dict__)
        return module
