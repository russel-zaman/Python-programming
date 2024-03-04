#This is the way to import a module/other function into main function

from my_module import my_func

my_func()

# this is the way call packages or subpackages

from MyMainPackage import SomeMainScript
from MyMainPackage.SubPackage import MySubScript

SomeMainScript.report_main()

MySubScript.sub_report()

