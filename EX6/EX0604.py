'''
# TASK 4. Visualization
performs an analysis & visualization of the Titanic data
- the survival rates of the passengers in the different classes 
(e.g., "What was the survival rate for people in the 3rd class?") 
- the percentage of this class in the overall population 
(e.g., "How many % of passengers had tickets in the 1st class?")

passenger class: categorical data type
bar chart: shows the values of different categories of data 
as rectangular bars with different lengths.
generate text-based bars:

== 1st Class ==
Total |**                  | 10.1%            
Alive |*****               | 25.7%
== 2nd Class ==
Total |*******             | 32.7%
Alive |*****               | 24.1%
== 3rd Class ==
Total |***********         | 57.2%
Alive |****                | 19.8%

output
- three parts for the 1st, 2nd, and 3rd class
- each part: show the total % of the passengers in this class ("Total"), 
- the survival rate for people that had tickets in this class ("Alive"). 
- full bar: 20 characters wide from | to |, 
- while an empty bar represents 0% and a full bar represents 100%. 
- Add the percentage to the right, rounded to one decimal digit 
and leave a space to the |.
- percentages need to be mapped to 20 characters for the visualization, 
so every character equals about 5%. Combine a division and a round 
to calculate how many characters need to be drawn, 
e.g., for 37.6% the calculation would be round(37.6/5), which is 8, 
so 8 characters need to be drawn. Fill the remaining characters with spaces.

You can assume that your function will be provided the same normalized input data as for the previous task. 
Unlike for the previous task though, you can assume this time that at least one passenger will exist per class 
to reduce the amount of corner cases that need to be considered in the implementation.

Note: While it is not strictly required to work on this task, 
we would like to encourage you to put all parts of the whole exercise together 
and use your .csv parser, normalizer, and this analysis/visualizer to investigate the actual distribution in the real dataset.
'''

'''
== 1st Class ==
Total |**                  | 10.1%            
Alive |*****               | 25.7%
== 2nd Class ==
Total |*******             | 32.7%
Alive |*****               | 24.1%
== 3rd Class ==
Total |***********         | 57.2%
Alive |****                | 19.8%
'''

#- full bar: 20 characters wide from | to |, 
#- while an empty bar represents 0% and a full bar represents 100%. 
# - Add the percentage to the right, rounded to one decimal digit 
# and leave a space to the |.
# - percentages need to be mapped to 20 characters for the visualization, 
# so every character equals about 5%. Combine a division and a round 
# to calculate how many characters need to be drawn, 
# e.g., for 37.6% the calculation would be round(37.6/5), which is 8, 
# so 8 characters need to be drawn. Fill the remaining characters with spaces.

def visualize(records):
    lst = records[1:][0]
    total = len(lst)
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0

    # access to each class & categorise  
    for i in range(len(lst)):
        # 1st class total
        if lst[i][1] == 1:
            # 1st class # of ppl
            n1 += 1

        # 1st class alive
        if lst[i][1] == 1 and lst[i][0] == True:
            n4 += 1

        # 2nd class total
        if lst[i][1] == 2:
            # 2nd class # of ppl
            n2 += 1

        # 2nd class alive
        if lst[i][1] == 2 and lst[i][0] == True:
            n5 += 1

        # 3rd class: total
        if lst[i][1] == 3:
            n3 += 1

        if lst[i][1] == 3 and lst[i][0] == True:
            n6 += 1

    # 1st class total percentage
    f_total = round(n1/total*100, 1)
    f_total_bar = '*'*round(f_total/5) + ' '*(20-round(f_total/5))
    # 1st class alive
    f_alive = round(n4/n1*100, 1)
    f_alive_bar = '*'*round(f_alive/5) + ' '*(20-round(f_alive/5))
    # 2nd class total percentage
    s_total = round(n2/total*100, 1)
    s_total_bar = '*'*round(s_total/5) + ' '*(20-round(s_total/5))
    # 2nd class alive
    s_alive = round(n5/n2*100,1)
    s_alive_bar = '*'*round(s_alive/5) + ' '*(20-round(s_alive/5))
    # 3rd class total
    t_total = round(n3/total*100, 1)
    t_total_bar = '*'*round(t_total/5) + ' '*(20-round(t_total/5))
    # 3rd class alive
    t_alive = round(n6/n3*100, 1)
    t_alive_bar = '*'*round(t_alive/5) + ' '*(20-round(t_alive/5))


    res = (f'== 1st Class ==\n'
    f'Total |{f_total_bar}| {f_total}%\n'
    f'Alive |{f_alive_bar}| {f_alive}%\n'
    f'== 2nd Class ==\n'
    f'Total |{s_total_bar}| {s_total}%\n'
    f'Alive |{s_alive_bar}| {s_alive}%\n'
    f'== 3rd Class ==\n'
    f'Total |{t_total_bar}| {t_total}%\n'
    f'Alive |{t_alive_bar}| {t_alive}%')

    return res


print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
    ]
)))


data = (
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        (True, 1, 'Some Name', 'female', 38, 71.2833),
        
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),
        (False, 1, 'Some Name', 'female', 38, 71.2833),

        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),
        (True, 2, 'Some Name', 'female', 38, 71.2833),

        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        (False, 2, 'Some Name', 'female', 38, 71.2833),
        
        (True, 3, 'Some Name', 'female', 38, 71.2833),
        (False, 3, 'Some Name', 'female', 38, 71.2833)*276
    ]
)

print(visualize(data))
# 20칸: 100 %
# 1칸: 5%
#print(37.6//5) # 8
#print(round(37.6/5,0))
#print(37.6 % 5)