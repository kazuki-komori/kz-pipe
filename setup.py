from setuptools import setup, find_packages

setup(
  name="kz_pipe",
  version="0.1.0",
  license="MIT",
  author="kazuki-komori",
  install_requires=[
    "pandas",
    "matplotlib_venn"
  ],
  packages=find_packages()
)