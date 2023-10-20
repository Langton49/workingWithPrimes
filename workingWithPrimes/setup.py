from setuptools import setup, find_packages

with open("Readme.md", "r") as f:
    long_description = f.read()

setup(
    name='wwp',
    version='1.1.1',
    description='Python module for working with prime numbers',
    author='Munashe',
    author_email='munashemukweya2022@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Langton49/workingWithPrimes',
    keywords='Prime, Numbers, Mathematics, Math',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.8.0',
        'numpy>=1.26.0',
    ],
    license="MIT",
    python_requires=">=3.10",
)
