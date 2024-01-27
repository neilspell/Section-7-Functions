# List of Names 👨🏽‍💻🤔

## Task 4 - List of Names

![SpongebobLongListGIF](SpongebobLongListGIF.gif)

### Part A
- Create a program that will allow the user to easily manage a list of names `names = []`.
- You should display a menu that will allow them to:
  - Add a name to the list
  - Change a name in the list
  - Delete a name from the list
  - View all the names in the list
- There must also be an option to allow the user to _End the Program_.

### Part B
If they select an option that is not in the menu, then display a suitable message.

After they have made a selection from the menu options, they should see the menu again, without having to re-start the program.

**_The program should be as user-friendly as possible._**

- Add suitable `#comments` to explain what your code is doing.


<details>
<summary>👀 Hint </summary>

````py
# Function definitions
def add_name():

def change_name():

def delete_name():

def view_names():


def main():
  again = "y"
  while again == "y":
    print("1) Add a name")
    print("2) Change a name")
    print("3) Delete a name")
    print("4) View names")
    print("5) Quit")
    selection = int(input("What do you want to do? "))
    if selection == 1:
      names = add_name()
      .
      .
      .
      .
      
# Main body of program

# Create empty list
names = []

# Call main() Function
main()
````
  
</details>