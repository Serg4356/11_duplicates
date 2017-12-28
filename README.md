# Anti-Duplicator

Programm searches for duplicates in catalog. It looks through all the files in current folder (and subfolders) and reports if it finds duplicates. Duplicates are two files with the same name and size.

# Quickstart

Programm takes one argument: path to folder.

Example of script launch on Windows, Python 3.5:

``` bash

$ python duplicates.py <path to file>

```

Example of programm output:

``` bash

$ python duplicates.py C:\devman\duplicates_test
File name: bars.txt| size: 4096 | Count of copies:  3 | Location:  ['C:\\devman\\duplicates_test', 'C:\\devman\\duplicates_test\\duplicates', 'C:\\devman\\duplicates_test\\duplicates\\duplicates2']

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
