import pkg1
#from dir1/dir2/file1 import func1
from pkg1.sub1.hello1 import hello1
from pkg1.sub1.hello2 import hello2
import sys

print(sys.path)

hello1()
hello2()
#The __init__.py in pkg2 will pre-import for you, so you don't need to 
#travel the full path.
from pkg2 import hello1
from pkg2 import hello2

hello1()
hello2()
