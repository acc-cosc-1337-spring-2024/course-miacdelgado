# This program calls the multiply_numbers function defined in the
# output.py file
import output

# This runs the numbers 6 and 6 through the function
result = output.multiply_numbers(6, 6)
print(result)


# This asks the user for two numbers and then runs them through
# the multiply numbers function
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a second number: '))
result = output.multiply_numbers(num1, num2)
print(num1, '*', num2, '=', result)