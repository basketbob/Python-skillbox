import os

file_name = 'testFile.txt'
directory = 'test_files'

path_file = os.path.join('..', '..', directory, file_name)
abs_path = os.path.abspath(path_file)
print(path_file)
print(abs_path)
print('-----------------------')

path = os.path.abspath('..')
list = os.listdir(path)
print(path)
print(list)
print('-----------------------')
print(os.getcwd())