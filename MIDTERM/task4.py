'''
Write a function count_positive_even_numbers 
which computes the number of positive even numbers in the first n numbers of a list.
'''

# count_positive_even_numbers([-2, -1, 2, 1, 4, 6, 8], 5) should return 2
# because among the first 5 numbers of the list, 2 and 4 are positive and even
def count_positive_even_numbers(numbers, n):
    count = 0
    for i in range(n):
        if numbers[i] > 0 and numbers[i] % 2 == 0:
            count += 1
    return count

print(count_positive_even_numbers([-2, -1, 2, 1, 4, 6, 8], 5))
print(count_positive_even_numbers([-2, -1, 2, 1, 4, 6, 8], 7))