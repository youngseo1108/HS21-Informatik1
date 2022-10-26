'''
# TASK 1. Read .csv Files
To store and exchange data between different programs, data is 
often stored in files using well-defined and reusable formats.
CSV: a record ("row") in the tabular data. attribute ("column") separated by comma

For instance, consider the following table:
Age	Gender	Weight (kg)	Height (cm)
28	Female	58	168
33	Male		188
...

in a .csv file:
Age,Gender,Weight (kg),Height (cm)
28,Female,58,168
33,Male,,188
...

read_csv
- parameter: the path to a file
- open arbitrary .csv files
- read the contents (parse the contents)
- convert the lines into a list of string tuples
- The different tuple indices: various attributes of the record

Several alternatives exist for encoding the .csv data, 
e.g., quoting attributes ("), adding spaces after each commas("..., ..."). 
- i.e., that every line has the same number of columns.
- attributes do not contain any quotes 
- different attributes do not contain commas
- ignore empty lines 
- empty attributes interpreted as an empty string, 
e.g., a line a,,c should be encoded as ("a","","c").

your function should return the following list:
[
    ("Age", "Gender", "Weight (kg)", "Height (cm)"),
    ("28", "Female", "58", "168"),
    ("33", "Male", "", "188")
]

Note: The .csv files often contain the headers as the first line. Make sure that this line is preserved.
Note: You can assume that provided files always exist. 
The implementation should be able to read empy files though, 
for which the result is simply an empty list.
'''
path1 = "D:/2021/Informatik1/ACCESS_21HS/EX6/example.csv"
path2 = "D:/2021/Informatik1/ACCESS_21HS/EX6/example1.csv"
path3 = "D:/2021/Informatik1/ACCESS_21HS/EX6/example2.csv"
path4 = "D:/2021/Informatik1/ACCESS_21HS/EX6/ac.csv"

# trial 2.
def read_csv(path):
    res = []
    with open(path, 'r') as file:
        for line in file.readlines():
            line = line[:-1]
            # read empty files -> result: an empty list.
            if len(line) == 0:
                continue
            res.append(tuple(line.split(',')))
    return res

print(read_csv(path1))
print(read_csv(path2))
print(read_csv(path3))
print(read_csv(path4))
# does not ignore empty lines at the start of a .csv file.