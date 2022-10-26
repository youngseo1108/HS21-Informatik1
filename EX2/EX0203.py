'''
The first program a developer writes in a new language is typically a 
"hello world" program to see a first output on the screen. 
In this task, you will create a more advanced version that can generate a 
more complex greeting.

Given the two variables name and age, write a program that will generate a 
personalized greeting. For example, for "Hans" and 37, the program should 
generate the string 

"Hello Hans, you are 37 years old!".

Implement it in a function generate_greeting where it should be returned.
'''
name = "Hans"
age = 37

# generate the greeting sentence
def generate_greeting():
    # You need to change the following line
    greeting = 'Hello ' + name + ', you are ' + str(age) + ' years old!'
    # You don't need to change the following line.
    # It simply returns the string created above.
    return greeting

print(generate_greeting())