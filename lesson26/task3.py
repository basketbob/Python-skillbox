import os


def gen_files_path():
    curr_dir = os.getcwd()
    list_files = os.listdir()
    for f in list_files:
        yield curr_dir + '/' + f

    return



for file_path in gen_files_path():
    file = open(file_path)

