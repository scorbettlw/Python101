"""
    Lesson 002 - Pt1: Introduction to String Variables

    Welcome to your second lesson! Let's start by reviewing some
    basics regarding variable declaration, assignment, and modificaton
    in Python.

"""


# Let's take a look at the variable below

username = "John Wick"

# A variable in Python is like a box with a label. You can store anything
# of the same type in that box, and you can combine and change what's
# in a given box (or in given boxes) via operations. In Python, a variable
# declaration is made up of three parts:
#
#   - Variable Name (the box label)
#
#   - = (the "assignment" operator, universal to almost any programming language,
#        which lets the Python interpreter know we're about to put something in the
#        box we created by declaring the variable name).
#
#   - Data (of a single type, aka the "content" or "stuff" in the box).
#
# Now, go ahead and create a variable called:
#
#   user_location
#
# below.
#

### CODE HERE: ###



# Note that with this variable, we used an "_" (underscore) character
# between different words. In Python (and most programming languages), any
# whitespace between characters denotes that a given segment of code (i.e.
# the variable declaration) has ended. Were we to seperate "user" and "location"
# with a space, Python would throw a Syntax Error, indicating that we've
# violated the programming language's "grammar" rules, such that the
# Python interpreter can't figure out how to run our code!
#
# Using an underscore to seperate words or parts of a variable name isn't
# the only way to declare such a variable of course. We could also declare
# the variable as "userLocation". This new method is called Camel Case, while
# the former (seperation by underscore) is called Snake Case. When writing Python,
# most programmers adhere to using Snake Case due to a language standard called
# PEP8, which is like a writing "style". Like any writing "style", PEP8 is not
# strictly enforced in Python, and should be confused with the syntax (the grammar)
# of the language. However, I highly recommend reading up on PEP8 once you've completed
# a few lessons. As with learning any writing style, while it's not necessary it can
# greatly improve the readability and "cleanliness" of your code!
#
# Now let's declare another variable. This time, I won't provide the exact label
# I want you to use. Using Snake Case, declare a variable using what you think is
# a good variable name (a good label) to store some data about our user's profession.
# Don't worry about what the profession itself is. As long as you follow the variable name
# with a space, then an equals, another space, and some sort of valid text surrounded by double
# quotes (i.e. like: "cook"), it'll work!

### CODE HERE: ###



# Excellent job! Now pull up your command shell and run the command:
#
#   python string_variables.py
#
# You shouldn't see any output yet. If you do see an error, take a step back and make sure the
# syntax for your variable declaration is correct. Now, let's discuss the important topic of
# variable reassignment. You "reassign" (overwrite) the data of a variable by "calling" (writing
# the name of the variable below its initial declaration) an already-declared variable and
# then assigning that variable to a different value like below:
#
# my_variable = "I am this."
#
#
# my_variable = "I am now this."
#
# Reassigning existing variables is a critical part of programming, as creating a new
# variable any time you needed to change something would be inefficient and tedious! However,
#
#   *if you reassign the data in a variable,
#   any code below that reassignment that uses
#   that variable will no longer have access to
#   the previous data stored in that variable.*
#

# Let's round out by introducing a key language feature, the:
#
#   print()
#
# method. A method can be thought of as a callable behavior, and thankfully Python's print
# method is built-in to the language itself. Calling the print method allows you to output program
# information (such as the data stored in a variable) to your command shell/prompt/console. To
# print the data stored in a variable you've created to the console simple write the name of the
# variable between the parenthesis of the print method like so:
#
#   print(user_location)
#
# Writing a variable name inbetween the parenthesis of a method is referred to as "passing" the variable
# to the method. When we "pass" the our:
#
#   user_location
#
# variable to the print method, Python executes logic behind the scenes that passes the String data we
# have stored in that variable to the method, and then outputs that data to our shell/console without
# us even having to lift a finger! Note that most functions require you to pass data of the appropriate
# data type or a variable containing valid data of the appropriate type, i.e.:
#
#   print("Hello world!")
#
# or:
#
#   message = "Hello world!"
#
#   print(message)
#
# However, many functions also allow you to pass additional data that changes the behavior of the method.
# When calling a method, that method has *parameters*, optional or required fields for which you must
# provide valid data of the appropriate type. Data passed to these *parameters* are called *arguments*.
# Arguments passed are seperated via commas. For example, with the print method, we may print the data
# contained within multiple arguments to console as below:
#
#   my_name = "Sean"
#
#   my_age = 27
#
#   print("Hello, my name is:", my_name, "and I am:", my_age)
#
# Go ahead and print both the:
#
#    username
#
# and:
#
#   user_location
#
# variables. Then test that this works by again running our program via the command:
#
#   python introduction_to_strings.py
#

### CODE HERE: ###



# As always, if you're lost or stuck, feel free to ask questions in the comments!