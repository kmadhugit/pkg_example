import setuptools,os
print(f'running pk1.pkg1_sub1.setup @ {os.getcwd()}')
setuptools.setup(
    name="pkg_example",
    version="0.1",
    author="madhusudanan kandasamy",
    author_email="madhukandasamy@yahoo.com",
    description="A small example package",
    url="https://github.com/kmadhugit/pkg_example.git",
    package_dir={'':'../../../'},
    packages=['pkg_example.pkg1.pkg1_sub1'],
    install_requires = [
        'flask'
        ]
)
