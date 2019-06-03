import setuptools

setuptools.setup(
    name="pkg-examples",
    version="0.1",
    author="madhusudanan kandasamy",
    author_email="madhukandasamy@yahoo.com",
    description="A small example package",
    url="https://github.com/kmadhugit/pkg_example.git",
    packages=['pkg1_sub1'],
    install_requires = [
        'flask'
        ]
)