from JTools.FileTools import *
#https://realpython.com/absolute-vs-relative-python-imports/
path = __file__[:-11]

'''
imports all of its freinds into this file hopefully
'''
p = File(path,True) # gets the files

for file in p.files:
    #print(file)
    if '__init__.py' in file: # ignores self
        continue
    else:
        if '.py' in file: # so you can have only other py files be imported into the projcet
            file = file.replace('.py','') # file we want to import
            #print('from .{} import *'.format(file))
            exec('from JTools.{} import *'.format(file)) # file that gets imported


  