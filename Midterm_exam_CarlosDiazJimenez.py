# Midterm Exam

# QUESTION X
# text text text actual question

print("QUESTION X")
# SOLUTION

# QUESTION 1
# What will be the value of "a" at the end of the code:
# a = 16
# a = a // 2
# print(a**2)
# a = a + 11
# print(a+1)
# a = a - 3

print("QUESTION 1")
# SOLUTION

a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

# QUESTION 2
# What will the following code print?
# print(2+3*6/2)

print("QUESTION 2")
#SOLUTION
print(2+3*6/2)

# QUESTION 3
# Fill in what the code below prints (all the lines):

print("QUESTION 3")
#SOLUTION
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

# QUESTION 4
# Here is a function that determines if a number is palindrome or not:

print("QUESTION 4")
#SOLUTION
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Which of the below is NOT a palindrome?
print(palindrome("4257304920394478392772938744930294037524"))
print(palindrome("7798338247658278460338648728567428338977")) # false
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("2704702208931031198668911301398022074072"))

# QUESTION 5
# Write a function that finds all the occurrences of a certain pattern, that starts with “un” has unlimited number of letters and ends with “an”
# The function takes 1 parameter: the text to look into and returns the number of matches.
# Use only the things we have learned in class. Give some explanations besides the code.

print("QUESTION 5")
#SOLUTION

def count_occurrences(text): #When we create a function we use "Def"
    words = text.split()  # Split the text into words using this method
    count = 0

    for word in words:
        if word[:2] == "un" and word[-2:] == "an": #we could also use methods with start and end but i fill more comfortable this way
            count = count + 1  # Increase count if condition is met

    return count  # Return the number of matches

# Example usage
text = "unbroken unchain unhuman unplan unknown unban"
print(count_occurrences(text))  # Should return 3 (unchain, unhuman, unplan)


# QUESTION 6
# Please explain what it means that a list is mutable and a string is not mutable (imutable).
# Give some code that shows the difference. Use your own words

print("QUESTION 6")
#SOLUTION

# strings - session 7&8
# lists - session 9&10
# Explanation:
# Mutability means that an object can be modified after it is created.
# Immutability means that an object cannot be changed after it is created.

# Lists are Mutable
#A list is mutable because you can change the items inside the list after it was created. This means we can:
#Add new elements.
#Remove elements.
#Change existing elements.

# Strings are Immutable
#This means that you can not change them once created.
#Trying to change will result in an error: TypeError: 'str' object does not support item assignment
#If we want to modify a string, we need to create a new string (an altered copy of a string). This works because slicing creates a copy, rather than changing the original

#CODE
# Lists are mutable
my_list = [1, 2, 3]
print("Original list:", my_list)

my_list[0] = 10  # Changing an element
print("Modified list:", my_list)

my_list.append(4)  # Adding a new element
print("List after append:", my_list)

# Strings are immutable
my_string = "hello"
print("\nOriginal string:", my_string)

# Trying to change a character directly (this will cause an error)
# my_string[0] = "H"  This is NOT allowed!

# Instead, we need to create a new string
new_string = "H" + my_string[1:]  # Creating a new string with modification
print("Modified string:", new_string)


# QUESTION 7
# Here si some code:
# Continue by replacing the numbers greater than 80 with their corresponding negative value (90 will be replaced with -90).
# Also replace the number lower than 40 with the sum of their digits: 39 is replaced by 12.
# print the list at the end
# Use only what we have learned in class. Provide some explanation in the form of comments.

print("QUESTION 7")
#SOLUTION

import random

random_numbers = [] #creating an empty list (bag)
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Step 2: Modify the list based on the conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]  # getting the number larger than 80 and make them negative
    elif random_numbers[i] < 40:

        num_str = str(random_numbers[i])  # Convert number into a string
        digit_sum = sum(int(digit) for digit in num_str)  # Sum all digits within the number
        random_numbers[i] = digit_sum  # Store the sum in the list

# Step 3: Print the modified list
print(random_numbers)



#QUESTION 8
# Write a function that checks if the passed parameter is a valid URL or not.
# Please also explain your reasoning. Use only the concepts that we learned in class.
# Do not use any imports

print("QUESTION 8")
#Solution

def checkwebsite(websitename):
    if websitename.startswith("https://"):  # First, check if the URL starts with "https://"
        if websitename.count(" ") == 0: #check if there are any spaces in the URL
            print("this URL is valid")
        else:
            print("invalid URL") # Both conditions met == "invalid URL"
    else:
        print("invalid URL") #If both conditions are not met == "invalid URL"

checkwebsite("https://holaadios")
checkwebsite("https://github.com/Carlosdiaz05/Midterm_exam")


# QUESTION 9
# Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since the day you were born (without counting the days in your birth year and the current year, so just whole years).
# The function takes your birthday as a parameter in string format.
# Do not import anything, use only what we learned in class

print("QUESTION 9")
#SOLUTION

def days_since_birthday(birthday):
    """
    Calculates the number of days that have passed since the user's birthday,
    excluding the birth year and the current year.

    :param birthday format "DD-MM-YYYY"
    :return: The number of days that have passed (excluding birth and current year)
    """
    birth_year = int(birthday[-4:])  # Last 4 characters are the year

    # Assume the current year is 2025
    current_year = 2025

    # Calculate whole years that have fully passed
    full_years_passed = (current_year - 1) - (birth_year + 1) + 1  # Excluding birth and current year

    # Multiply by 365 to get the total number of days
    total_days = full_years_passed * 365
    return total_days

print(days_since_birthday("28-03-2005"))

#Counting leap years
def days_since_birthday(birthday):
    """
    Calculates the number of days that have passed since the user's birthday,
    excluding the birth year and the current year, accounting for leap years.

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: The number of days that have passed (excluding birth and current year)
    """
    birth_year = int(birthday[-4:])  # Last 4 characters are the year

    # Assume the current year is 2025
    current_year = 2025

    # Calculate whole years that have fully passed
    full_years_passed = (current_year - 1) - (birth_year + 1) + 1  # Excluding birth and current year

    # Count leap years within the range
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # Only count full years
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1

    # Multiply by 365 for normal years and add extra days for leap years
    total_days = (full_years_passed * 365) + leap_years
    return total_days

print(days_since_birthday("28-03-2005"))

