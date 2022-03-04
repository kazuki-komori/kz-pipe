from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="kz_pipe",
    version="0.1.0",
    license="MIT",
    author="kazuki-komori",
    install_requires=_requires_from_file('requirements.txt'),
    packages=find_packages()
)