'''
The "International Fixed Calendar" (IFC) propose to replace the common Gregorian Calendar with a more regularly-paced alternative. 

One variant of the IFC works like this:
- Every month has exactly 28 days (exactly 4 weeks).
- There are 13 months in a year (13*28 = 364).
- The year ends with a special "Year Day", which does not belong to any month or week.
- In leap years, the year ends with two "Year Days".

- takes a gregorian date as two integers day (between 1 and 31) and month (between 1 and 12) 
as well as an optional boolean is_leap as parameters. 
-> indicates, whether you're dealing with a leap year that has 366 days and is False by default 
(you may change the signature to set the default value). 
- convert the given date to an IFC-date. 
- return the resulting day and month in the IFC calendar as as a tuple. 
- For the end of the year, the function should return the String "Year Day". 
Consider the assertions given below as examples for using gregorian_to_ifc.
'''

def gregorian_to_ifc(day, month, leap = False):
    if day > 28:
        day -= 28
        month += 1
        return (day, month)

    if day == 30 and month == 12 and leap == True:
        return 'Year Day'

    if day == 31 and month == 12 and leap == False:
        return 'Year Day'
    return (day, month)    

# DO NOT SUBMIT THE LINES BELOW!
assert gregorian_to_ifc(1, 1) == (1, 1)
assert gregorian_to_ifc(28, 1) == (28, 1)
assert gregorian_to_ifc(29, 1) == (1, 2)        # 29th Jan Gregorian is 1st Feb IFC
#assert gregorian_to_ifc(1, 3) == (4, 3)         # 1st  Mar Gregorian is 4rd Mar IFC
#assert gregorian_to_ifc(29, 2, True) == (4, 3)  # leap year
#assert gregorian_to_ifc(1, 8) == (17, 8)
#assert gregorian_to_ifc(15, 11) == (11, 12)
#assert gregorian_to_ifc(30, 12) == (28, 13)
#assert gregorian_to_ifc(30, 12, True) == "Year Day"
#assert gregorian_to_ifc(31, 12) == "Year Day"