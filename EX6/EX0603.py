'''
TASK 3. Data Analysis

Attribute	Type	Expected schema	                        Fix Action
Survived	boolean	True for survived, False otherwise	    Discard
Pclass	    int	    only values 1, 2, and 3 are allowed	    Discard
Name	    string	the name	                            Discard
Gender	    string	only "male" and "female" are allowed	Discard
Age	        float	Age in the range [0.0, 100.0]	        Discard
Fare	    float	The ticket fare is a positive float	    Replace with 25.0

The data
- 1st element: a tuple with all keys 
- 2nd element: a list that contains all records as normalized tuples

Task
- partition the data 
1) Passengers' class, 
2) Passengers' gender
- calculates the passengers distribution according to gender & class
- results: arranged in two nested tuples. More specifically, t[0][1] should contain the rate of passengers that were holding second class ticket and were male:

(
	("First class and male", "Second class and male", "Third class and male"),
	("First class and female", "Second class and female", "Third class and female")
)

- Calculate the percentages in the range of 0, 100
with a precision of one number of decimal. 
e.g. 45 passengers in 123 passengers = 45/123 = 0.3658...~36.6% of the population (float, use round)

Note: the provided dataset is valid and always contains at least one entry.
though the dataset does not contain data for all six values -> return None
'''

def gender_class_rates(dataset):
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    lst = dataset[1][0:]
    total = len(lst)

    if total == 0:
        return None

    for i in range(len(lst)):
        # 1st class women
        if lst[i][1] == 1 and lst[i][3] == 'female':
            n4 += 1
        # 1st class men
        if lst[i][1] == 1 and lst[i][3] == 'male':
            n1 += 1

        # 2nd class women
        if lst[i][1] == 2 and lst[i][3] == 'female':
            n5 += 1
        # 2nd class men
        if lst[i][1] == 2 and lst[i][3] == 'male':
            n2 += 1
        
        # 3rd class women
        if lst[i][1] == 3 and lst[i][3] == 'female':
            n6 += 1
        # 3rd class men
        if lst[i][1] == 3 and lst[i][3] == 'male':
            n3 += 1

    if n1 != 0:
        n1 = round(n1/total*100,1)
    else:
        n1 = None

    if n2 != 0:
        n2 = round(n2/total*100,1)
    else:
        n2 = None

    if n3 != 0:
        n3 = round(n3/total*100,1)
    else:
        n3 = None


    if n4 != 0:
        n4 = round(n4/total*100,1)
    else:
        n4 = None

    if n5 != 0:
        n5 = round(n5/total*100,1)
    else:
        n5 = None

    if n6 != 0:
        n6 = round(n6/total*100,1)
    else:
        n6 = None

    res1 = (n1, n2, n3)
    res2 = (n4, n5, n6)
    return tuple([res1,res2])

print(gender_class_rates((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        # ...
    ]
)))