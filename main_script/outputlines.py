from os import path

path_to_file = input('Please provide location of target file: ')
number = input('Please add amount for lines: ')


def print_paths_parts(file, number):

    """
        This method outputs print b amount of parts of input path to file 
        in correct order.
        Amount of parts also an input argument
        Works on with all common type of path : Unix and Win

        :parameters:
            path : string - path to be sliced
            number : int -  amount of last lines of file

        :returns :
            None
    """
    number = int(number)

    if path.isfile(path_to_file):
        print('Path file is valid. Yeah this is path to file' + '\n')
        with open(file, 'r') as file:
            file_lines = file.readlines()
            for i in reversed(range(1, number+1)):
                # Print last N lines of file in correct order
                print(file_lines[-i])
    else:
        print('Sorry - path to file doesn`t exist.Please provide another file')
