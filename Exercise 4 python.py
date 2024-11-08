# Question 1: Using a for loop with a list

# TODO: Create a lfruitist of fruits
fruit=("banana", "watermelon", "avocado", "apple")
for fruit in list(fruit) :
# TODO: Use a for loop to print each fruit in the list
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5 
while count > 0:
 print(count)
 count -= 1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for number in range(1,11):
  print(number**2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

# TODO: Create a list of colors
colours=("black", "blue", "purple")
# TODO: Use a for loop to select and print 3 random colors from the list
for colours in list(colours):
   print(colours)
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print(math_operations.add(4,5))
print(math_operations.subtract(4,5))
print(math_operations.multiply(4,5))
print(math_operations.divide(4,5))
# TODO: Use a while loop to create a simple calculator
