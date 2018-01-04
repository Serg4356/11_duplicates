import os
import sys


def create_file_location_dictionary(path):
    files_location_dictionary = {}
    for file_paths, dirs, files in os.walk(path):
        for file_name in files:
            file_location = '{}\nSize: {}'.format(
                file_name,
                str(os.path.getsize(os.path.join(file_paths, file_name))))
            files_location_dictionary.setdefault(file_location,[]).append(file_paths)
    return files_location_dictionary


if __name__ == '__main__':
    try:
        path_to_dir = sys.argv[1]
        if not bool(os.path.isdir(path_to_dir)):
            sys.exit('Please enter correct path to folder')
        print('Duplicates:\n')
        file_location_dictionary = create_file_location_dictionary(path_to_dir)
        for file_name, file_locations in file_location_dictionary.items():
            if len(file_locations) > 1:
                print('File name: {}\nCount of copies: {}\nLocation: \n{} \n\n'.format(
                    file_name,
                    len(file_locations),
                    '\n'.join(file_locations)
                ))
    except IndexError:
        print('Please, enter path to folder.')
