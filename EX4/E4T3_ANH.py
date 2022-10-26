import os

def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False

    if os.stat(path_reading).st_size == 0:
        with open(path_reading,'r') as reading, open(path_writing,'w') as writing:
            writing.write(reading.read())
            #return writing
    else:
        with open(path_reading,'r') as reading, open(path_writing,'w') as writing:
            for line in reading.readlines():
                if line.startswith('Name'):
                    writing.write('Firstname,Lastname\n')
                if line == "\n":
                    writing.write(',\n')
                    continue
                space = line.find(' ')
                symbol = line.find(';')
                if space > 0 and symbol > 0:
                    writing.write(line[symbol+2:] + ',' + line[0:symbol])
                elif space > 0 or symbol == 0:
                    writing.write(line[0:space] + ',' + line[space+1:])
        return path_writing

print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/my_data.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed1.txt"))
print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/name.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed2.txt"))
print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/empty.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed3.txt"))
print(process_data("D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/conversion.txt", "D:/2021/Informatik1/ACCESS_21HS/EX4/EX0403/processed4.txt"))