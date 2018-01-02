import os
import sys


def create_file_location_dictionary(path):
    file_location_dictionary = {}
    for file_paths, dirs, files in os.walk(path):
        for file in files:
            file_location_dictionary.setdefault(
                '{} | size: {}'.format(
                    file,
                    str(os.path.getsize('{}\\{}'.format(
                        file_paths,
                        file
                    )))
                ), []
            ).append(file_paths)
    return file_location_dictionary


def find_duplicates(file_location_dictionary):
    duplicates_message = 'Duplicates:\n'
    for file_name, file_location in file_location_dictionary.items():
        if len(file_location_dictionary[file_name]) > 1:
            duplicates_message += (
                'File name: {} \n Count of copies: {} \n Location: {} \n'.format(
                    file_name,
                    len(file_location),
                    file_location)
            )
    return duplicates_message


if __name__ == '__main__':
    file_location_dictionary = create_file_location_dictionary(sys.argv[1])
    print(find_duplicates(file_location_dictionary))
