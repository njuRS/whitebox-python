import os
import sys

#当前工作路径
print (os.getcwd())

#相对路径表达一个文件
file = 'examples/testdata/DEM.tif'
#获取这个文件的绝对路径
print (os.path.abspath(file))

#获取当前.py文件所在的路径
print (sys.path[0])

#如果当前.py文件所在的路径不是当前工作路径，则更新
if os.getcwd() != sys.path[0]:
    os.chdir(sys.path[0])

#更新成功
print (os.getcwd())

print ('ok')

