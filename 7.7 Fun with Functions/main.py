# ---------------------------
# Title: Fun with Functions
# Date:
# ---------------------------

#task 2
'''def findAverage(x,y,z):
  total = x+y+z
  average = total/3
  return average


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

result = findAverage(num1, num2, num3)

print("Average is: ", result)'''

'''#task 3
def askValue():
  num = int(input("Enter a number: "))
  return num
  

# We must pass the value of num as an argument to count().
def count(num):
  n = 1
  while n <= num:    # loop through all number 1 -> num
    print(n)
    n = n+1    # increment by 1 each time

# The count() function, takes a number as an argument and prints a sequence of numbers.

def main():
  num = askValue()  # Calls asValue() function and assigns it to num
  count(num)        # Calls count() function and passes

main()'''

# Function definitions
def add_name():
  name = input("Enter a new name: ")
  names.append(name)
  return names

# Function to change name in the list
def change_name():
  num = 0
  for x in names:
    print(num, x)
    num = num + 1
  select_num = int(input("Enter the number of the name you want to change: "))
  name = input("Enter new name: ")
  names[select_num] = name
  return names


# Function to delete name from the list
def delete_name():
  num = 0 
  for x in names:
    print(num, x)
    num = num + 1
  select_num = int(input("Enter the number of the name you want to delete: "))
  del names[select_num]
  return names




# Function to view the List of Names
def view_names():
  for x in names:
    print(x)
    
  print()

# Function to display menu and select options
def main():
  again = "y"
  while again == "y":
    print("*** Menu Options ***")
    print("1) Add a name")
    print("2) Change a name")
    print("3) Delete a name")
    print("4) View names")
    print("5) Quit")
    selection = int(input("What do you want to do? "))
    if selection == 1:
      add_name()
    elif selection == 2:
      change_name()
    elif selection ==  3:
      delete_name()
    elif selection == 4:
      view_names()
    elif selection == 5:
      again = "n"
    else:
      print("Incorrect option: ")
     
      
# Main body of program

# Create empty list
names = []

# Call main() Function
main()