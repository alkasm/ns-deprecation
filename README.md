# namespace deprecation test

This is a trial to figure out how to insert a subpackage into a namespace package, with backwards compatibility and deprecation warnings.

### Have

Here we have a namespace package `nstest` with subpackages `pkg_a` and `pkg_b`:

```python
>>> from nstest.pkg_a.a import a
>>> from nstest.pkg_b.b import b
>>> print(a, b)
a b
```

### Want

```python
>>> from nstest.pkgs.pkg_a.a import a
>>> from nstest.pkgs.pkg_b.b import b
>>> print(a, b)
a b
```

### Soft deprecation, with backcompat

```python
>>> from nstest.pkg_a.a import a
<stdin>:2: FutureWarning: referencing `nstest.pkg_a` is deprecated; use `nstest.pkgs.pkg_a` instead
>>> from nstest.pkg_b.b import b
<stdin>:2: FutureWarning: referencing `nstest.pkg_b` is deprecated; use `nstest.pkgs.pkg_b` instead
>>> print(a, b)
a b
```

### Hard deprecation, with help text

Keep the old package name around, but only to throw a useful error.

```python
>>> from nstest.pkg_a.a import a
ModuleNotFoundError: No module named 'nstest.pkg_a.a'. Did you mean 'nstest.pkgs.pkg_a.a'?
```

### Some ideas

#### Stubbed `__init__.py`

If `pkg_a` and `pkg_b` are not namespace packages, then we can stub them out inside `nstest` and have them reference `nstest.pkgs`, e.g.

```python
# nstest/pkg_a/__init__.py
import warnings
warnings.warn("referencing `nstest.pkg_a` is deprecated; use `nstest.pkgs.pkg_a` instead")

from nstest.pkgs.pkg_a import a as a
```

But this doesn't work for namespace packages, because they don't have an `__init__.py`.

#### Stubs for every module

Could instead provide stubs for _every_ module.

```python
# nstest/pkg_a/a.py
import warnings
warnings.warn("referencing `nstest.pkg_a` is deprecated; use `nstest.pkgs.pkg_a` instead")

from nstest.pkgs.pkg_a.a import *
```

Do type stubs work in this case as well?

Yes, they do! However, this does not work if you programmatically import via `importlib` or `__import__`. It all probably works if you simply import the module, but not if you `from module import *`, which we need to do if we want to alias that module. To alias it properly, we'd need to update `globals()` with the module's contents, and mypy does _not_ understand that.

#### pkgutil-style namespace packages

This might provide another solution as well, but I haven't looked into it. Not sure how/if it would affect existing subpackages and so on.
