'''
TASK 2. Data Preprocessing
data: CSV format, each row = passenger with the following attributes

Attribute	Description
Survived	Whether the passenger survived or not
Pclass	    Ticket class of the passenger
Name	    Name of the passenger
Gender	    Gender of the passenger
Age	        Age of the passenger
Fare	    Fare paid by the passenger

- a missing or corrupted data point:
Attribute	Type	Expected schema	                        Fix Action
Survived	boolean	True for survived, False otherwise	    Discard
Pclass	    int	    only values 1, 2, and 3 are allowed	    Discard
Name	    string	the name	                            Discard
Gender	    string	only "male" and "female" are allowed	Discard
Age	        float	Age in the range ]0.0, 100.0]	        Discard
Fare	    float	The ticket fare is a positive float	    Replace with 25.0

- input: a list of string tuples
(1) convert each attribute to its intended data type, 
(2) normalize the values by making sure the values for every attribute are consistent with the expected schema, 
(3) handle missing and corrupt values with the corresponding fix action. 
- the first line of a .csv file is the header -> unchanged

- return a tuple of
1) the tuple that contains all header keys and 
2) a list of normalized value tuples that are consistent with the schema. For example, consider the following example as an illustration:

preprocess([
	("Survived", "Pclass", "Name", "Gender", "Age", "Fare"),
    ("survived", "1", "Bukater Ms. Rose", "f", "17", "200"),
	("No", "3", "Dawson Mr. Jack", "male", "", "")
])
# should result in 
(
	('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
    	(True, 1, "Bukater Ms. Rose", "female", 17.0, 200.0)
    ]
)

Note: Understanding the data is an important step in every data analysis task, 
so download and investigate the provided file titanic.csv to understand what you are working with. 
Most importantly, do not confuse invalid data with inconsistent data. 
For instance, the column Gender contains mixed values such as 'Female', 'female', or 'f'. 
These values are inconsistent with our expected schema, but they are valid. 
Treat such cases differently than invalid data to preserve as much of the data as possible.
'''
def preprocess(records):
    header = records[0]
    data = []

    alive = ['Alive', 'survived', 'Survived', 't', 'T', 'yes', 'Yes', 'TRUE', 'True', 'true']
    dead = ['dead', 'Dead', 'F', 'f', 'no', 'No', 'Survived=dead', 'FALSE', 'False', 'false']
    male = ['m', 'male', 'M', 'Male']
    female = ['female', 'f', 'Female', 'F']

    for e in records[1:]:
        lst = []
        # survived / bool
        if e[0] in alive:
            lst.append(True)
        elif e[0] in dead:
            lst.append(False)
        else:
            continue

        # ticket class / int
        if not e[1]:
            continue
        if int(e[1]) in [1,2,3]:
            lst.append(int(e[1]))
        else:
            continue

        # name / string
        if not e[2]:
            continue
        else:
            lst.append(e[2])

        # gender / string
        if e[3] in female:
            lst.append('female')
        elif e[3] in male:
            lst.append('male')
        else:
            continue

        # age / float
        if not e[4]:
            continue
        if 0.0 <= float(e[4]) <= 100.0:
            lst.append(float(e[4]))
        else:
            continue

        # ticket / float
        if not e[5]:
            lst.append(25.0)
        else:
            if float(e[5]) >= 0:
                lst.append(float(e[5]))
            else:
                lst.append(25.0)
        
        data.append(tuple(lst))
    return (header, data)


titanic = [
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
    ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
    # ...
]

test =  ([
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
            ('Dead', '3', 'Braund Ms. Maria', 'Female', '21', ''),
            ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
            ('', '3', 'Vander Planke Miss. Augusta', 'female', '', ''),
            ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')])


#expected = (('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
#            [
#                (False, 3, 'Braund Mr. Owen Harris', 'male', 22.0, 7.25),
#                (False, 3, 'Braund Ms. Maria', 'female', 21.0, 25.0),
#                (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38.0, 71.28)
#            ]
#        )

print(preprocess(titanic))
print(preprocess(test))
