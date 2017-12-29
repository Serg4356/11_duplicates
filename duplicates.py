import os
import sys


def create_file_location_dictionary(path):
    file_location_dictionary = {}
    for paths, dirs, files in os.walk(path):
        for file in files:
            file_location_dictionary.setdefault(file + '| size: '
                                                + str(os.path.getsize(paths + '\\' + file)), []).append(paths)
    return file_location_dictionary


def find_duplicates(file_location_dictionary):
    duplicates_message = 'Duplicates:\n'
    for key, value in file_location_dictionary.items():
        if len(file_location_dictionary[key]) > 1:
            duplicates_message += ('File name: {} \n Count of copies: {} \n Location: {} \n'.format(key, len(value), value))
    return duplicates_message


if __name__ == '__main__':
    path_to_folder = input('Enter path to folder:\n')
    try:
        file_location_dictionary = create_file_location_dictionary(path_to_folder)
        print(find_duplicates(file_location_dictionary))
    except IndexError:
        print('Please, enter the path to folder')