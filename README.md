# pkg_example
python distribution example


# Test whether setup works fine locally.
* python3 setup.py sdist bdist_wheel .  
(or)
* pip install .

# push and install via git

* pip install git+https://github.com/kmadhugit/pkg_example.git
* if you want to keep a local copy in the directory where you run pip.
* pip install -e git+https://github.com/kmadhugit/pkg_example.git#egg=MyProject

# install from a sub directory or release or commit.
Read the below link
* https://pip.readthedocs.io/en/stable/reference/pip_install/#git

* pip install git+https://github.com/kmadhugit/pkg_example.git@v1.0




# verify
* python -m site

* pip list |  grep pkg

* pip show pkg-examples




# delete
pip unistall doesn't work, please check.  
https://stackoverflow.com/questions/21306954/how-to-remove-pip-package-after-deleting-it-manually
# manual uninstall
* find all installed files in sitepackage_dir/xxx_info/RECORD
* delete all of them.
* verify with pip list and pip show.


