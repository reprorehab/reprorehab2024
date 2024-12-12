# Write a for loop to print out numbers 1 to 10.
for number in range(10):
    print(number+1)

# Write a while loop that starts with a variable x = 0 and keeps adding 1 to x until x is greater than 5. Print the value of x after each iteration. 
x = 0
while x <= 5:
    x+=1
    print(x)

# Write a loop to print out the even numbers from 1 to 20 using an  if statement
should_stop, n_iter, MAX_ITER = False, 0, 20
while not should_stop:
    n_iter += 1
    if n_iter % 2 == 0:
        print(n_iter)
    should_stop = n_iter == MAX_ITER

# Fizz Buzz problem from week 4 except incorporate at least one nested if statement. Test number 15 and print "FizzBuzz".
n = 15
if n % 3 == 0:
    if n % 5 == 0:
        print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")

# Write a function that prints 1 if the input is ‘hello’, 0 if the input is ‘world’, and -1 if the input is ‘!’ (use match-case)
def breaking_hello_world(string: str):
    if string == 'hello':
        print(0)
    elif string == 'world':
        print(1)
    elif string == "!":
        print(-1)
        
print(breaking_hello_world('hello'))
print(breaking_hello_world('world'))
print(breaking_hello_world('!'))

# Write a function that takes a list of booleans and returns True if any are True 
def is_any_true(boolean_list):
    if any(boolean_list):
        return(True)
    else:
        return(False)
        
print(is_any_true([True, True, True]))
print(is_any_true([True, False, True]))
print(is_any_true([False, False, False]))


# Write a function that takes a list of boolean and returns True if all are True 
def is_all_true(boolean_list):
    if all(boolean_list):
        return(True)
    else:
        return(False)
        
print(is_all_true([True, True, True]))
print(is_all_true([True, False, True]))
print(is_all_true([False, False, False]))

# Write a function that takes a list of strings and returns True if the list contains the string ‘apples’
def looking_for_apples(GROCERY_LIST):
    if 'apple' in GROCERY_LIST:
        return True
    else:
        return False
        
SHOPPING_LIST = ['honey crisp apples', 'banana', 'chocolate almonds']
print(looking_for_apples(SHOPPING_LIST))

# Write a function that takes a list of strings and returns True if the list does not contain the string ‘apples’
def not_looking_for_apples(GROCERY_LIST):
    if 'apple' not in GROCERY_LIST:
        return True
    else:
        return False
        
NEW_SHOPPING_LIST = ['honey crisp apples', 'banana', 'chocolate almonds']
print(not_looking_for_apples(NEW_SHOPPING_LIST))

# Define a variable total = 0. Write a for loop that iterates through the list values = [1, 2, 3, 4], adding each value to the total variable. Print the total after the loop completes.
total = 0
for value in [1, 2, 3, 4]:
    total = total + value
    print(total)

#  Write a for loop that directly accesses and prints each element from the list colors = ['red', 'blue', 'green', 'yellow'] without using the range() function.
colors = ['red', 'blue', 'green', 'yellow']
for color in colors:
    print(color)

# Initialize an empty list new_list = []. Use a for loop to append the squares of numbers from 1 to 5 to new_list. Print new_list after the loop finishes
new_list = []
for number in range(5):
    new_list.append(number+1)
print("Updated list: ", new_list)

# Given a 2D list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write a for loop that prints each element in the matrix. Print each row on a new line.
# Hint:  use a nested for loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# attempt 1
for row in matrix:
    for value in row:
        print(value)
        
# attempt 2
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        value = matrix[row_index][col_index]
        print(value)