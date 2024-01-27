# Files and Functions 📚

![AgentSmithGIF](AgentSmithGIF.gif) 


The following problem is broken into two parts:

## Part A 👨🏽‍💻
Create the following Display Menu that will appear in the console.

````
--- Company Salaries ---
1) Add to file
2) View all records
3) Quit program

Please select an operation (1 - 3): 
````
1. If the user selects 1, allow them to add to a file called `Salaries.csv` which will store their name and annual salary.
2. If they select 2, your program should display all records in the `Salaries.csv` file.
3. If they select 3, it should stop the program.
4. Should the user enter an incorrect value, display an error message and return them to the Display Menu.



## Part B 👨🏽‍💻
In Python, it is not technically possible to directly delete a record from a `.csv` file. 

Instead, you must create a _temporary list_ in Python and then overwrite the original file with the temporary list.

1. Change the previous program to allow you to do this.
2. Your Display Menu should now look something like this...

````
--- Company Salaries ---
1) Add to file
2) View all records
3) Delete a record
4) Quit program

Please select an operation (1 - 4): 
````

As always, please include suitable `# comments` to explain what your code is doing.
  