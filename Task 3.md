# Task 3 👨🏽‍💻

The following code is a simple implementation of a function.

````py
# Create an empty list
people = []

# Create a function to put people on the list
def get_person():
    # What does this line do?
    person_name = input("What is their name?")    
   # What does this line do?
    return person_name

# What does this line do?
person_count = int(input("How many people would you like to add?"))

# What does this loop do?
for count in range(person_count):
    people.append(get_person())

# What does this line do?
print("You've added ", person_count, " people!")
print("Here they are: ", people)
````

## PRIMM 🔍✍🏽
1. Copy and paste the code above into `main.py`.
2. _PREDICT_ the output of the code with your classmate. 
3. Now _RUN_ the code to test your prediction.
4. Explain what `return person_name` does?
5. Add `# comments` to the sample code to explain what each line does.

<details>
  <summary> Explanation 👀 </summary> 
  
In the provided Python program, the purpose of `return person_name` within the `get_person()` function is to return the name of the person entered by the user back to the caller. 

This returned value is then _appended_ to the `people` list.

### Here's a step-by-step explanation of how the program works:

1. An empty list called `people` is created at the beginning.

2. The `get_person()` function is defined, which collects information about a person's name using the `input()` function. The collected name is stored in the `person_name` variable.

3. The `return` statement is used to pass back the value of `person_name` to the caller (the loop that appends names to the `people` list).

4. The program then asks the user how many people they would like to add. The input is stored in the variable `person_count`.

5. A `for` loop runs `person_count` times, and in each iteration, it calls the `get_person()` function to get a person's name from the user and appends it to the `people` list.

6. After the loop, the program prints the number of people added (`person_count`) and the contents of the `people` list.

For example, if the user enters `3` for `person_count` and provides the names "Alice," "Bob," and "Charlie" as inputs, the output would be:

```
What is their name?Alice
What is their name?Bob
What is their name?Charlie
You've added 3 people!
Here they are: ['Alice', 'Bob', 'Charlie']
```

Each name is collected using the `get_person()` function and added to the `people` list. The final list contains the names of all the people added.
 
</details>


## Extra Credit ✨
1. Add a function ``def add_age`` that will get the _age_ from the user.
2. Modify the ``for`` loop to call ``add_age`` and _append_ it to a new list``age[]``.

>
> 