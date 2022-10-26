'''
TASK 3. Data processing

A friend of yours is asking for help with a task in Excel. 
In your friends' spreadsheet there is a column with the header 
Name, which contains first names and last names in each cell in 
two different formats. However, your friend needs the first names 
and last names in two separate columns with the headers 
Firstname and Lastname, respectively.

write a function process_data, which reads the data from the original 
file my_data.txt and writes a file my_data_processed.txt with the 
converted data in comma-delimited format. 
In the original file names are stored in two different formats.

1st format: firstname<SPACE>lastname / Fred Brooks.
2nd format: lastname<SEMICOLON><SPACE>firstname / Euler; Leonhard.
Comma-delimited means that there is a delimiter which separates 
the data values. 
In this task the delimiter in the desired output is the comma 
and the values separated are firstname and lastname. 
If a line is empty (as in, it contains only the newline character \n)
in the original file, then the line in the output file should contain
only a comma. See the example below for a better understanding.

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

The output of your function should adhere to these additional rules:
- input file X exist -> return False & not write any output file
- input file exists but empty -> empty output file
- only contains the header (Name) -> only headers Firstname,Lastname.
- The last line of the output file should not contain the trailing newline character (\n).
You can assume that the last line in the input file will never be an empty line.
'''
import os

def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # input file does not exist, the function should return False & not write any output file.
        return False
    # input file O, but empty -> an empty output file
    with open(path_reading, 'r') as f:
        lines = f.readlines()
        with open(path_writing, 'w') as file:
            if len(lines) == 0:
                file.write('')
            # only header (Name) -> a file with only headers Firstname,Lastname.
            elif len(lines) == 1:
                file.write('Firstname,Lastname')
        
            else:
                for line in lines:
                    if 'Name' in line:
                        file.write('Firstname,Lastname\n')
                    elif line == '\n':
                        file.write(',\n')
                    else: # last line: x contain the newline character (\n)
# 문제: 뒤에꺼 + 앞에꺼로 하면서 이름 + '\n' 다음 줄에 성이 출력되는 거였음!
                        if ';' in line: #Berger; Roland -> Roland,Berger
                            str = line.strip('\n')
                            idx = str.find(';')
                            file.write(str[idx+2:] + ',' + str[:idx])
                            if line != lines[-1]:
                                file.write('\n')
                        else:
                            file.write(line.split(' ')[0] + ',' + line.split(' ')[1])
    
    with open(path_writing, 'r') as f_check:
        lines_check = f_check.readlines()
    f.close()
    file.close()
    return lines_check

# Conversion was not correct for file: Name\nTim Li\nAl; Bea\n\n\nBi; Flo


print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/my_data.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed1.txt"))
print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/name.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed2.txt"))
print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/empty.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed3.txt"))
print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/conversion.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed4.txt"))