from folder_as_a_module import myfile

myfile.f()


from folder_as_a_module import *  # '__all__ = ["myfile"]' in __init__.py

myfile.f()


import folder_as_a_module # 'from . import myfile' in __init__.py

folder_as_a_module.myfile.f()
