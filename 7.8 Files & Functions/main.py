# -----------------
# Title: 
# Date:
# -----------------


import csv

# Function to add Name & Salary to .csv file
def addtoFile():
    name = input("Enter Name: ")
    salary = int(input("Enter Annual Salary: "))
    newRecord = name + ", " + str(salary) + "\n"

    # Using 'with' statement for file handling, append name + salary to .csv file
    with open("Salaries.csv", "a") as file:
        file.write(newRecord)

# Function to read .csv file
def viewRecords():
    # Using 'with' statement for file handling, read contents of .csv file
    with open("Salaries.csv", "r") as file:
        print("\nContents of File:")
        for row in file:
            print(row)

# Function to delete data from .csv list
def deleteRecord():
    # Using 'with' statement for file handling, read contents of .csv file
    with open("Salaries.csv", "r") as file:
        x = 0
        temp_List = []  # Create a temporary empty list

        for row in file:  # Iterate through file and add contents to temp_List
            temp_List.append(row)         
        file.close()

        for row in temp_List:  # Print file data with numeric reference
          print(x, "->", row)
          x = x + 1

        row_to_delete = int(input("Enter the row number to delete: "))
        del temp_List[row_to_delete]
      
    # Using 'with' statement for file handling
    # Write data from temp_List back into Salaries.csv
    with open("Salaries.csv", "w") as file:
        for row in temp_List:  # Iterate through temp_List sending data back to Salaries.csv
          file.write(row)
        file.close()

# Main body of program
tryagain = True
while tryagain is True:
    print("--- Company Salaries ---")
    print("1) Add to file")
    print("2) View all records")
    print("3) Delete a record")
    print("4) Quit program")
    print()

    selection = input("Please select an operation (1 - 4): ")
    if selection == "1":
        addtoFile()
    elif selection == "2":
        viewRecords()
    elif selection == "3":
        deleteRecord()
    elif selection == "4":
        tryagain = False
    else:
        print("!!! Invalid Option Selected - Please Try Again. !!! \n")
