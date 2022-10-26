'''
Implement a function stats, which takes a parameter students, a dictionary. 
The variable raw in the template below is a valid example.

Every key in students is a matriculation number as a string. 
Every value is a list of tuples, where the first element is a subject as a string and the second element is a grade between 1 and 6.

The function shall return two values, both dictionaries.
The first dictionary should be a mapping from matriculation number to the average grade of the relevant student. 
The second dictionary should be a mapping from school subject to the average grade of all students in that subject. 
The average grades should be rounded to two decimal places.

You can assume that the function is only called with valid parameters.
'''

def stats(students):
# The first dictionary should be a mapping from matriculation number to the average grade of the relevant student. 
# The second dictionary should be a mapping from school subject to the average grade of all students in that subject. 
    individual_avg = {}
    subject_avg = {}
    appear = {}
    for k,v in students.items():
        total_individual_grade = 0
        for e in v:
            total_individual_grade += e[1]
            if e[0] not in subject_avg:
                subject_avg[e[0]] = e[1]
                appear[e[0]] = 1
            else:
                subject_avg[e[0]] += e[1]
                appear[e[0]] += 1
        individual_avg[k] = round(total_individual_grade / len(v), 2)
    
    for k in subject_avg.keys():
        subject_avg[k] = round(subject_avg[k] / appear[k], 2)
    return individual_avg, subject_avg
# DO NOT SUBMIT THE LINES BELOW!
raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
	"09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
	"01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
	}
students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)

print(subjects)