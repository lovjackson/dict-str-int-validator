from functools import wraps
from collections.abc import Mapping

def ensure_dict_str_int(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        def _validate(arg, name: str):
            if not isinstance(arg, Mapping):
                raise TypeError(f"{name} must be dict[str, int], got {type(arg).__name__}")
            for k, v in arg.items():
                if not isinstance(k, str):
                    raise TypeError(f"{name}[{k!r}] key must be str, got {type(k).__name__}")
                if not isinstance(v, int):
                    raise TypeError(f"{name}[{k}] value must be int, got {type(v).__name__}")

        for i, arg in enumerate(args):
            _validate(arg, f"args[{i}]")
        for k, v in kwargs.items():
            _validate(v, f"kwargs['{k}']")
        return func(*args, **kwargs)
    return wrapper
