import os
import sys


def find_duplicates(path):
    file_dict = dict()
    for paths, dirs, files in os.walk(path):
        for file in files:
            file_dict.setdefault(file + '| size: ' + str(os.path.getsize(path)),[]).append(paths)
    for key in file_dict.keys():
        if len(file_dict[key]) > 1:
            print('File name: ' + key, '| Count of copies: ', len(file_dict[key]), '| Location: ', file_dict[key])


if __name__ == '__main__':
    try:
        find_duplicates(sys.argv[1])
    except IndexError:
        print('Please, enter the path to folder')