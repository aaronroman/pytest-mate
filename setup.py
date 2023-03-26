from setuptools import setup, find_packages

setup(
    name="pytestmate",
    version="0.0.1",
    packages=find_packages(where="src/**"),
    include_package_data=True,
    python_requires=">=3.8",
    entry_points={"console_scripts": ["pytestmate=src.main:main"]},
)
