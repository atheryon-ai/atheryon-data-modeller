from setuptools import setup, find_packages

setup(
    name="agent",
    version="0.1.0",
    packages=find_packages(include=["agent", "agent.*"]),
)