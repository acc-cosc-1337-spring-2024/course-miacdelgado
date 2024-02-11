# This imports the functions from the decisions.py file
import decisions

# Gather contents of option and total
option = float(input('Please enter the amount of options: '))
total = float(input('Please enter the total amount: '))

result = decisions.get_options_ratio(option, total)

print(decisions.get_faculty_rating(result))
