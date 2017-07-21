import os
_root = os.getcwd()
for root, dirs, files in os.walk(_root):
    if root != _root:
        break  
    for name in files:
        print '* [%s](%s)' % (name[:-3], name) 
