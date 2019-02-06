import pkg1
from pkg1.sub1.hello1 import hello1
from pkg1.sub1.hello2 import hello2
import sys

print(sys.path)

hello1()
hello2()
