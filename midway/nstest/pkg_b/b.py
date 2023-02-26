from nstest.pkgs.pkg_b.b import *
import warnings as _warnings

_new_package = "nstest.pkgs" + __package__.removeprefix("nstest")
_warnings.warn(
    f"referencing {__package__} is deprecated; use {_new_package} instead",
    FutureWarning,
    stacklevel=2,
)
