from setuptools import find_namespace_packages, setup

setup(
    name="nstest-pkgs",
    packages=find_namespace_packages(where="nstest*"),
    package_data={"": ["py.typed", "*.pyi"]},
    extras_require={"dev": ["mypy"]},
)
