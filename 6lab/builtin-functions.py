def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))  



def count_case_letters(s):
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    return upper_case, lower_case

s = "Hello World"
upper, lower = count_case_letters(s)
print("Прописные:", upper)  
print("Строчные:", lower)   
 


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

s = "A man a plan a canal Panama"
print(is_palindrome(s))  



import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = delayed_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")



def all_true(t):
    return all(t)

t = (True, True, True)
print(all_true(t))
t = (True, False, True)
print(all_true(t))
























