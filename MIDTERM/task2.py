'''
Write a function swap_case that takes a string as the input parameter 
and returns the same string with inverted cases. 
So lowercase characters should be transformed to uppercase and vice versa.
Make sure the function works on the empty string as well.
'''
# swap_case("HElLO, woRLd!") should return "heLlo, WOrlD!"
def swap_case(s):
    if len(s) == 0:
        return s
    else:
        res = ''
        for ch in s:
            if ch.islower():
                res += ch.upper()
            else:
                res += ch.lower()
        return res

print(swap_case("HElLO, woRLd!"))
print(swap_case(''))