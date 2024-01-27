# --------------------------
# Title: Nested Conditionals
# Date:
# --------------------------


'''age = int(input("Enter age: "))


if age < 17:
  print("You are too young.")
elif age >= 17:
  provisional_licence = input("Do you have a Provisional. Enter Y / N: ") # prompt user about licence
  if provisional_licence == "Y":
    print("Elligible to apply")
  else:
    print("You cannot apply. You need a Provisional") 

'''

carAge = int(input("Enter age of car: "))
fuelType = input("Is it Deisel or Petrol: ")

if carAge >= 10 or fuelType == "Diesel":
  print("Pollution Level - High")
else:
  print("Pollution Level - Low")

