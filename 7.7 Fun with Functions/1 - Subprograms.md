# Subprograms 📚 

`Subprograms` (Functions) are blocks of code which perform simple tasks and can be called upon at any time in a program to run that code.

> Examine the following code and see if you can understand what it is doing:

````py
def get_name():
  userName = input("Enter your name: ")
  return username

def print_Msg(userName):
print("Hello", userName)

def main();
  userName = get_name()
  print_Msg(userName)

main()

````

## Task 1 - Predict, Run and Debug
- Turn to your classmates and see if you can explain what the 3 Subprograms (Functions) are doing.
- In `main.py` run the code to see if your prediction was correct.
- You may need to de-bug the code 🪲.

<details>

<summary> 📝 What's going on?</summary>

Obviously, there is no need to create such a convoluted way of performing this simple program. 

This example is used to illustrate how Subprograms / Functions are laid out and how ``variables`` can be used & passed between the Functions.
  
</details>

## 💡Note:
Python does not like surprises.

If you are going to use a Function in a program, Python must have read the function definition `def function_name()` first, so it knows where to find it. 

If you try to refer to a Function before Python has read about it, it panics and crashes! 

The funtion definition `def function_name()` must be written **_ABOVE_** the function call `function_name()`.
