# -------------------------
# Title: Intro to Functions
# Date:
# -------------------------


'''def volOfCylinder(r,h):
  vol = 3.14*(r**2)*h
  print(vol)


# get radius and height from User
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

volOfCylinder(radius, height)'''





# Task 3
# Create an empty list
people = []
age = []

# Create a function to put people on the list
def get_person():
    # Collect information about the person
    person_name = input("What is their name?")    
    # Give back the person
    return person_name

# Create a function to add ages to a list
def add_age():
   # Collect age of person
    age = input("What is their age?")    
    # Give back the age
    return age

# Here's a short program using the functions
person_count = int(input("How many people would you like to add?"))
for count in range(person_count):
    people.append(get_person())
    age.append(add_age())
  
print("You've added ", person_count, " people!")
print("Here they are: ", people)
print("Here are their ages: ", age)
