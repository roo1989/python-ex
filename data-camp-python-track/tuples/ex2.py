"""
Making tuples by accident

Tuples are very powerful and useful, and it's super easy to make one by accident. All you have to do is create a variable and follow the assignment with a comma. This becomes an error when you try to use the variable later expecting it to be a string or a number.

You can verify the data type of a variable with the type() function. In this exercise, you'll see for yourself how easy it is to make a tuple by accident.
Instructions
100 XP

    Create a variable named normal and set it equal to 'simple'.
    Create a variable named error and set it equal 'trailing comma',.
    Print the type of the normal and error variables.

"""

normal = 'simple'
error  = 'trailing comma',

print(type(normal))
print(type(error))
