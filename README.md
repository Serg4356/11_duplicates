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

$ python duplicates.py G:\devman\dup_test
Duplicates:

File name: 1.txt
Size: 67
Count of copies: 3
Location: 
G:\devman\dup_test
G:\devman\dup_test\some_folder
G:\devman\dup_test\some_folder2

File name: bars.txt
Size: 413166
Count of copies: 2
Location: 
G:\devman\dup_test
G:\devman\dup_test\some_folder2

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
