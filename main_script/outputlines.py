from os import path


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

    if not path.isfile(file):
        print('Sorry - path to file doesn`t exist.Please provide another path')
    else:
        with open(file, 'r') as file:
            file_lines = file.readlines()
            max_number = len(file_lines)
            if number > max_number:
                print("Sorry, amount of number is bigger than amount of lines.\
                      Amount in provided file is {}".format(max_number), sep='')
            else:
                for i in reversed(range(1, number+1)):
                    # Print last N lines of file in correct order
                    print(file_lines[-i])


print_paths_parts('test_file.txt', 2)