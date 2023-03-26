from setuptools import setup, find_packages

setup(
    name="pytest-mate",
    version="0.1.1",
    packages=find_packages(where="src/**"),
    include_package_data=True,
    entry_points={"console_scripts": ["pytestmate=src.main:main"]},
)
