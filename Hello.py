import os
import imghdr
import subprocess
import sys
from subprocess import *
import shutil
import fileinput
import logging
from os import path

'''
Doc String
'''

#testing
'''
#### MAP Function#######
ding = []
area = ['1','3','5']
def fun(x):
    x = x * 4
    return x
for i in area:
    ding.append(fun(i))
print ding
print "Using Map Function"
print list(map(fun,area))
'''

def ExecuteCmd(cmd):
    try:
        (stdout, stderr)=("","")
        proc= subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout,stderr = proc.communicate()
    except :
        print sys.exc_info()

    return stdout,stderr

######Directory Function######--- Printing only Images
'''
def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names

for i in walk("/Users/arunkkr/Downloads/"):
    if imghdr.what(i) != None:
        print i

###### Funtion to check only HTML Files

for i in walk("/Users/arunkkr/Documents/OPSS"):
    cmd = "file " + i
    output = ExecuteCmd(cmd)
    #print i
    try:

        if output and "HTML" in output[0].split(":")[1].strip("\n"):
            print output[0].split(":")[0]
            print "Copying File :"+i
            shutil.copy(output[0].split(":")[0],"/Users/arunkkr/Documents/OPSS/html")
    except:
        print "Something Wrong with this File:"+i
sys.exit()

Ding = "/Users/arunkkr/Downloads/Learning/interact-6.33.1_hf4"
print "Item's path: " + str(path.realpath(Ding))
print "Item's path and name: " + str(path.split(path.realpath(Ding)))
print "base"+str(os.path.basename(Ding))

##### Logging #######
logging.basicConfig(filename='mylogs.txt',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)
logging.debug("This is Debug Logging")
logging.info("This is Info Logging -->"+Ding)
logging.warn("This is Warn Logging")
logging.error("This is Error Logging")
logging.critical("This is Critical Logging")
'''

b = ['121','1232','21132']
a = range(1,4)
for i in a:
    try:
        if b[i] == '':
            break
        else:
            print b[i]
    except:
        print sys.exc_info()[1]

#### File Append######
'''
def replace_line(file_name,line_num,text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

replace_line('/Users/arunkkr/nullfromaddress.txt',15, 'DingoArun')

'''
'''
with open('test.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(' Ding ', ' Arun ')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)

'''

### Enumerate Function####

### zip Function ###

### Try catch Final Else Function###

### set function ####

#TODO: Testing Todo
print("The End of Python Function")
print9


