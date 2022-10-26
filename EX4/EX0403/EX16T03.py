'''
A friend of yours is asking for help with a task in Excel. 
In your friends' spreadsheet there is a column with the header Name,
which contains first names and last names in each cell in two different formats.
However, your friend needs the first names and last names in two separate columns with the headers Firstname and Lastname, respectively.

You decide to help your friend, so you need to write a function process_data which reads the data from the original file my_data.txt 
and writes a file my_data_processed.txt with the converted data in comma-delimited format. 
In the original file names are stored in two different formats.

The first format can be described as firstname<SPACE>lastname, for example Fred Brooks.
The second format looks like lastname<SEMICOLON><SPACE>firstname, for example Euler; Leonhard.
Comma-delimited means that there is a delimiter which separates the data values. In this task the delimiter in the desired output is the comma and the values separated are firstname and lastname. If a line is empty (as in, it contains only the newline character \n) in the original file, then the line in the output file should contain only a comma. See the example below for a better understanding.

Example of an input file:

Name
Beat Meier

Barbara Suter
Berger; Roland
The corresponding output file should contain:

Firstname,Lastname
Beat,Meier
,
Barbara,Suter
Roland,Berger

Your function should adhere to these additional rules:
- If the input file does not exist, the function should return False and not write any output file.
- If the input file does exist, but is empty, an empty output file should be written.
- An input file that only contains the header (Name) should result in a file that contains only the headers Firstname,Lastname.
- The last line of the output file should not contain the trailing newline character (\n).
- You can assume that the last line in the input file will never be an empty line.
Note: To check for the existence of a file, you can use import os, followed by a os.path.exists(«path»). 
This snippet is already included in the template, you just have to decide what to do in case the file does not exist.
Hint: The function find can help for this task.
'''
import os

def process_data(path_reading, path_writing):
    # If the input file does not exist, the function should return False and not write any output file.
    if not os.path.exists(path_reading):
        return False
    # If the input file does exist, but is empty, an empty output file should be written.
    with open(path_reading, 'r') as reading, open(path_writing, 'w') as writing:
        header = reading.readline()
        # If the input file does exist, but is empty, 
        # an empty output file should be written.
        if header == '':
            return None
        # An input file that only contains the header (Name) 
        # should result in a file that contains only the headers Firstname,Lastname.  
        if header.find('\n') != -1:
            writing.write('Firstname,Lastname\n')
        else:
            writing.write('Firstname,Lastname')

        for line in reading.readlines():
            # case1: lastname;firstname // Berger; Roland -> Roland,Berger
            idx_semicolon = line.find(';')
            if idx_semicolon != -1:
                if line.find('\n') != -1:
                    firstname = line[idx_semicolon+2:-1]
                    lastname = line[:idx_semicolon] + '\n'
                else:
                    firstname = line[idx_semicolon+2:]
                    lastname = line[:idx_semicolon]
                writing.write(f'{firstname},{lastname}')

            # case2: empty line
            elif line == "\n":
                writing.write(",\n")

            # case3: firstname lastname
            else:
                idx_space = line.find(' ')
                firstname = line[:idx_space]
                lastname = line[idx_space+1:]
                writing.write(f'{firstname},{lastname}')
    # An input file that only contains the header (Name) should result in a file that contains only the headers Firstname,Lastname.
    # The last line of the output file should not contain the trailing newline character (\n).
    # You can assume that the last line in the input file will never be an empty line.

print(process_data("my_data.txt", "my_data_processed.txt"))