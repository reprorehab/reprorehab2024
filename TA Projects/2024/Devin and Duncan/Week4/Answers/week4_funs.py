import typing

def sum_values(a: int, b: int) -> int:
    # This function take in two integers (a and b) and return the sum of these integers 
    print(a)
    return a + b

def is_upper_case(letter: str) -> bool:
    # This function takes a scalar string and returns True if it is upper case and False if it is lower case 
    if letter.isupper():
        return True
    else:
        return False

def add_element_if_unique(initial: typing.List[str], new_element: str) -> typing.List[str]:
    # This function takes a list of strings and a string. It will return a 
    # new list that appends the new string to the list only if it is not already part of the list.
    if new_element in initial:
        return initial
    else:
        return initial.append(new_element)

def fizz_buzz(n: int) -> str:
    # This is a classic programming problem. 
    # This function takes an integer and returns the string Fizz if the integer 
    # is divisible by 3, Buzz if the integer is divisible by 5, FizzBuzz if the 
    # integer is divisible by both 3 and 5, and None otherwise.
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
