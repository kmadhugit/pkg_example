import setuptools
#If there is no __init__.py in pkg1 directory, it won't be identified as package
#setup tools will not included it in the distribution

setuptools.setup(
    name="pkg-examples",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
)
