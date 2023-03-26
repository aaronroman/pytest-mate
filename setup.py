from setuptools import setup, find_packages

setup(
    name="pytestmate",
    version="0.1.0",
    packages=find_packages("src/**"),
    include_package_data=True,
    entry_points={"console_scripts": ["pytestmate=src.main:main"]},
)
