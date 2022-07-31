from setuptools import setup, find_packages

setup(
    name="src",
    author="ouss",
    author_email="ouss.miss@gmail.com",
    description="movies jobs",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
