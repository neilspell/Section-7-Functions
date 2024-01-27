# ----------------------
# Title:
# Date:
# ----------------------

'''# Task 1
def display_happyBday():
  print("Happy Birthday")

# Call the function 3 times
for i in range(3):
  display_happyBday()

print()
# Task 2
def multiply_and_display(num1, num2):
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")

# Test the function with example inputs
multiply_and_display(5, 7)

print()
'''
# Task 3
def are_strings_identical(str1, str2):
    return str1 == str2

string1 = "Hello, World!"
string2 = "Hello, World!"
string3 = "Hello, Python!"

print(are_strings_identical(string1, string2))  # Output: True
print(are_strings_identical(string1, string3))  # Output: False


# Task 4
def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_str = input_str.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return input_str == input_str[::-1]

# Ask the user to enter a word
user_input = input("Enter a word: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")