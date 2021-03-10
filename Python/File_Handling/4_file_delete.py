from os import remove
from os.path import exists

file_path = 'files/my_first_file.txt'

if exists(file_path):
    remove(file_path)
else:
    print("File already deleted")
