import setuptools
import os
module_dir = os.path.dirname(os.path.abspath(__file__))
pdir =  f'{module_dir}/../'
print(f'cwd = {os.getcwd()} package_dir={pdir}')

setuptools.setup(
    name="mod1_sub1",
    version="0.1",
    author="madhusudanan kandasamy",
    author_email="madhukandasamy@yahoo.com",
    description="mod1 sub1 package",
    url="https://github.com/kmadhugit/pkg_example.git",
    package_dir={'':f'{pdir}'},
    packages=['mod1_sub1'],
    install_requires = [
        'base@git+https://github.com/kmadhugit/pkg_example.git#"subdirectory=base"'
        ]
)
