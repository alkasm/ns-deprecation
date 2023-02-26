import typing

from nstest.pkg_a.a import a
from nstest.pkg_b.b import b

assert a == "a"
assert b == "b"

if typing.TYPE_CHECKING:
    reveal_type(a)
    reveal_type(b)
