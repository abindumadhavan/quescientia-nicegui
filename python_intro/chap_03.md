# Chapter 3: Control Structures
        
Control structures allow you to control the flow of your program. Common control structures in Python include if statements, for loops, and while loops.
                
##### Control Structures

Control structures allow you to control the flow of your program. The most common control structures in Python are `if` statements, loops (`for` and `while`), and methods/functions.

1. An `if` statement allows you to execute a block of code only if a certain condition is true. For example:"

    > x = 10
    >
    > if x > 0:
    >
    >       print('x is positive')
    >
    > else:
    >
    >       print('x is not positive')

    This will print 'x is positive' if x is greater than 0, otherwise it will print 'x is not positive'.

2. You can also use `elif` to check multiple conditions:
   
    > x = -5
    >
    > if x > 0:
    > 
    >       print('x is positive')
    > 
    > elif x < 0:
    >       
    >       print('x is negative')
    > 
    > else:
    >       
    >       print('x is zero')

    This will print 'x is negative' if x is less than 0, 'x is zero' if x is equal to 0, and 'x is positive' if x is greater than 0.

##### Loops

Loops allow you to repeat a block of code multiple times

1. A `for` loop allows you to iterate over a sequence (like a list or a string). For example:")
    
    > for i in range(5):
    >
    >     # This will iterate from 0 to 4
    >
    >     print(i)  
    >
    >     # This will print the value of i in each iteration

    This will print the numbers 0 to 4.


2. A `while` loop continues to execute as long as a condition is true. For example:")

    > x = 5
    > 
    > while x > 0:  
    >
    >       # This will continue as long as x is greater than 0
    >
    >       print(x)
    >
    >       x -= 1  
    >
    >       # This will decrease the value of x by 1 in each iteration
    >

    This will print the values of x from 5 to 1.

##### Functions

1. Functions are reusable blocks of code that perform a specific task. You can define a function using the `def` keyword. For example:") 

    > def greet(name):
    >
    >       print(f'Hello, {name}!')  
    >       # This will print a greeting message with the name provided
    >       # You can call the function like this:
    > 
    > greet('Alice')  
    >       # This will output: Hello, Alice!

You can call the function `greet` with different names to greet different people.

In this chapter, we have covered the basics of Python programming, including variables, data types, control structures, loops and functions. These concepts are fundamental to writing Python programs and will be used throughout the course.
In the next chapter, we will explore data structures such as lists and dictionaries. Stay tuned!