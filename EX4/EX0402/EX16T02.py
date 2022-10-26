'''
In this task, you will create a small program that helps you with keeping track of your study results. 
You can write down your grades into a simple text file. 
This text file should contain one line per course. 
The line starts with the name of the course (string), followed by your grade after a colon (float).

To make it easier to maintain this file, the syntax is not very strict. 
It should be possible to use tabs and spaces before or after the colon, to have empty lines, 
and to write comments by starting a line with a #. 

Please consider the following file as an example:

# first semesters
Informatik 1:5.75
Informatik 2: 5.5

# later
Advanced Software Engineering : 6.00

Your task is to write a function get_average_grade. 
- takes the path to such a file as the argument 
- and reads it according to the rules mentioned before. 
- calculate the average for all the grades in the file and return it as the result. 
-> In the above example, calling the function should return 5.75. 
-> Return None, if the file does not exist
-> and 0.0 if the file does not contain any grades.

Note: To check for the existence of a file, you can use import os, followed by a os.path.exists(«path»). 
This snippet is already included in the template, you just have to decide what to do in case the file does not exist.
'''
#!/usr/bin/env python3

import os

def get_average_grade(path):
    # Return None, if the file does not exist 
    if not os.path.exists(path):
        return None
    # read the file according to the rule
    total = 0
    count = 0
    
    with open(path, 'r') as f:
        lines =  f.readlines()
        for line in lines:
            if line.startswith('#'):
                continue

            idx = line.find(':')
            if idx > 0:
                score = float(line[idx+1:])
                total += score
                count += 1

        if total == 0:
            return 0.0
        return total / count

print(get_average_grade("my_grades.txt"))