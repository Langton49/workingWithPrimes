from setuptools import setup, find_packages

setup(
    name='wwp',
    version='1.0.0',
    description='Python module for working with primes',
    author='Munashe Mukweya',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.8.0',
        'numpy>=1.26.0',
    ],
    license="MIT",
)
