import util
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = '.'
suffix = None
if len(sys.argv) > 2:
    suffix = sys.argv[2]
    
files = util.io.ls(path, suffix)
print(len(files)) 