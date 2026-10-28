"""Compatibility shim for basicsr on newer torchvision.

torchvision 0.17 removed torchvision.transforms.functional_tensor, which
basicsr (<=1.4.2) still imports. Importing this module first re-creates the
module name from torchvision.transforms.functional so basicsr loads.
"""
import sys
import types

try:
    import torchvision.transforms.functional_tensor  # noqa: F401
except ImportError:
    from torchvision.transforms import functional as _F

    _shim = types.ModuleType("torchvision.transforms.functional_tensor")
    for _name in dir(_F):
        if not _name.startswith("__"):
            setattr(_shim, _name, getattr(_F, _name))
    sys.modules["torchvision.transforms.functional_tensor"] = _shim
