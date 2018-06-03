#!/usr/bin/python
import os


def stripNumbers(file_name):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabetical_chars = [char for char in file_name if char not in numbers]
    return ''.join(alphabetical_chars)


def solvePuzzleInImages():
    dir_prefix = "/Users/visharma/Projects/nanodegree/lesson3/prank/"
    file_list = os.listdir(dir_prefix)
    for file_name in file_list:
        stripped_file_name = stripNumbers(file_name)
        os.rename(dir_prefix + file_name, dir_prefix + stripped_file_name)

    new_file_list = os.listdir(dir_prefix)
    for file_name in new_file_list:
        with open(dir_prefix + file_name) as f:
            lines = f.readlines()
            print lines


if __name__ == "__main__":
    solvePuzzleInImages()