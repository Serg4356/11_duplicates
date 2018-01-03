import os
import sys


def create_file_location_dictionary(path):
    file_location_dictionary = {}
    for file_paths, dirs, files in os.walk(path):
        for file_name in files:
            file_location = '{}\nSize: {}'.format(
                file_name,
                str(os.path.getsize('{}\\{}'.format(file_paths, file_name))))
            file_location_dictionary.setdefault(file_location,[]).append(file_paths)
    return file_location_dictionary


def find_duplicates(file_location_dictionary):
    for file_name, file_location in file_location_dictionary.items():
        if len(file_location_dictionary[file_name]) <= 1:
            file_location_dictionary.pop(file_name)
    return file_location_dictionary


def create_duplicates_message(duplicates):
    duplicates_message = ''
    for file_name, file_location in duplicates.items():
        duplicates_message += 'File name: {}\nCount of copies: {}\nLocation: \n{} \n\n'.format(
            file_name,
            len(file_location),
            '\n'.join(file_location)
        )
    return duplicates_message

if __name__ == '__main__':
    try:
        path_to_dir = 'G:\devman\dup_test'
        if not bool(os.path.isdir(path_to_dir)):
            print('Please enter correct path to folder')
            sys.exit()
        print('Duplicates:\n')
        file_location_dictionary = create_file_location_dictionary(path_to_dir)
        duplicates = find_duplicates(file_location_dictionary)
        print(create_duplicates_message(duplicates))
    except IndexError:
        print('Please, enter path to folder.')
