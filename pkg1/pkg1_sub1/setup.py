import setuptools
import os
from os.path import dirname
module_dir = dirname(__file__)
root_dir = f'{module_dir}/../../../'
os.chdir(root_dir)
print(f'running pk1.pkg1_sub1.setup @ {os.getcwd()} root_dir={root_dir}')

setuptools.setup(
    name="pkg_example",
    version="0.1",
    author="madhusudanan kandasamy",
    author_email="madhukandasamy@yahoo.com",
    description="A small example package",
    url="https://github.com/kmadhugit/pkg_example.git",
    #package_dir={'':'../../'},
    packages=['pkg_example.pkg1.pkg1_sub1'],
    install_requires = [
        'flask'
        ]
)
