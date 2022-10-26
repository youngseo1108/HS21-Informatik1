a = 'Youngseo Kim'


f,l = a.split(' ', 1)
print(f)
print(l)


txt = "apple#banana#cherry#orange"
x, y = txt.split("#", 1)
print(type(x))


path_reading = "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/conversion.txt"
path_writing = "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed4.txt"

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
                    file.write('\n,')
                else: # last line: x contain the newline character (\n)
                    if ';' in line: #Berger; Roland -> Roland,Berger
                        str = line.strip('\n')
                        idx = str.find(';')
                        file.write(str[idx+2:] + ',' + str[:idx])
                    else:
                        file.write(line.split(' ')[0] + ',' + line.split(' ')[1])

with open(path_writing, 'r') as f_check:
    lines_check = f_check.readlines()
    print(lines_check)