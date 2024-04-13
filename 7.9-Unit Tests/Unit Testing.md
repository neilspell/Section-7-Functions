# Unit Tests 📚

![image](https://github.com/ross-bish/Section-7-Functions/assets/83789503/c895386e-1cac-4820-868e-9681a45343dd)

![image](https://github.com/ross-bish/Section-7-Functions/assets/83789503/db517c93-4930-4866-93e8-d141a0a28ad6)

## Challenge ⚔️

Let's try to replicate the single unit test & multiple test cases from the book.

### Single Test 📝
This is the function that we are going to test.

````py
def volCylinder(radius, height):
  volume=3.14 * (radius**2) * height
  return volume
````
1. As the function to be tested `volCylinder(radius, height)` has 2 **arguments**, we need to create 2 variables with smaple values to be tested.

````py
testR = 2
testH = 1
````

2. Next we we must calculate the expected result for the volume of a cylinder with those values of ``radius = 2``, ``height = 1``.

````py
expectedVal = 3.14 * (testR**2) * testH
````
3. Now, when calling our function to test, we pass `testR` and `testH` as **arguments** to the `volCylinder()` function and store the returned value as a variable names `testANS`

````py
testAns = volCylinder(testR, testH)
````

4. We now need to check that the value returned from our function matches the expected value. We can create a **Boolean** variable named `passed` to record if the test passed or failed.

If the expected value does not match the actual value returned from the function, `passed` is set to `False`.

````py
passed = True
if expectedVal != testAns:
  passed = False
````

5. Finally, the value in `passed` is returned to the main program body using
````py
return passed
````

6. Using the sample code above, complete the `unitTest()` function.

💡**Note:** Dont forget to call your `unitTest` function in your main program body and display the value of `passed`.

````py
print("Test passed: ", unitTest() )
````


### Multiple Test Cases 📝
We will now look at automating the unit test for multiple test cases.

This time we will test a function called `largerNumber()`, which requires 2 arguments and returns teh larger of teh 2 numbers. This function uses logic, meaning their is more scope / possibility for errors than in the previous example.

### Make Task 👨🏽‍💻
Create a function called `largerNumber()` that will return the larger of 2 numbers.

<details>

  <summary>👀No peeking</summary>
  
````py
def largerNumber(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

````

</details>

1. Let's create 2 lists of values to be tested

````py
checkList_1 = [1, 2, 3, 4, 5]
checkList_2 = [1, 1, 4, -1, 100]

````
💡**Note:** The range of values to be tested goes from `-1` to `100`. Each item in `checkList_1` is greater than, less than or equal to the corresponding item in `checkList_2`.

2. Now, using a `for` loop, loop through each corresponding item in both lists, passing them into your `largerNumber()` function as arguments.

   The returned value from the function is stored as a variable named `testAns`.

3. While still in the loop, check that the value returned from `largerNumber()` matches the expected value.

<details>

  <summary>👀Hint:</summary>
  
Use a variable called `fails` as a counter to keep track of the number of test cases that fail (if any).

</details>
 

