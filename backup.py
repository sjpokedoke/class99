import os
import shutil

source = input('Enter the source folder name:')
dest = input('Enter the destination folder name:')

source = source+'/'
dest = dest+'/'

files = os.listdir(source)

for file in files:
    shutil.copy((source+file), dest)
    