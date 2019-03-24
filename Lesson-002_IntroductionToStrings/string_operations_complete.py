"""
    Lesson 002 - Pt3: String Operations I

    We explored the basics of declaring String-type variables and
    proper String syntax last time, now let's introduce a couple of
    the basic operations you can use to change (mutate) String-type
    data in variables!

"""

# We can do better than a simple:
#
#   username
#
# variable. Instead, let's create two new variables, and then combine
# then using operators and operations to create the full username! To begin,
# create two String-type variables (declared using proper Snake Case) called:
#
#   first_name
#
# and
#
#   last_name
#

### CODE HERE: ###

first_name = "Samuel"

last_name = "Jackson"


# Once declared, go ahead and check by printing both variables to console/shell:

### CODE HERE: ###

print(first_name)

print(last_name)


# and then running our program via the command:
#
#   python string_operations.py
#

# Now let's introduce our first operator and operations. If you've even
# touched grade school maths, you'll know the addition operator:
#
#   +
#
# In programming, the purpose of the "plus" becomes a little more complex. With
# number types like Integers and Floats, the plus retains its traditional purpose
# (adding the values of two numbers together). With Strings, it serves the different
# purpose of *concatenating* (combining) two Strings from left to right. For
# example, concatenating:
#
#   first_name = "John"
#
# and:
#
#   last_name = "Wick"
#
# variables would produce "JohnWick". Likewise, concatenating:
#
#   first_name = "John "
#
# and
#
#   last_name = " Wick"
#
# would produce "John Wick" (note the importance of the trailing space in the:
#
#   first_name
#
# variable's data). When concatenating strings, you can choose to either assign
# the result of that operation to a new variable or modify the data contained
# within an existing variable "in place". Assigning to a new variable works
# as below:
#
#   username = first_name + last_name
#
# while "in place" assignment works as below:
#
#   first_name  = first_name + last_name
#
# Note that "in place" assignment (reassignment) of a variable will overwrite the
# data stored in that variable, so any code below that "in place" assignment will
# only have access to the new data. Go ahead and assign the concatenation of your:
#
#   first_name
#
# and
#
#   last_name
#
# variables to a new variable called:
#
#   full_name
#
# below, print your new:
#
#   full_name
#
# variable to console, and then run the program via the command:
#
#   python string_operations.py
#

### CODE HERE: ###


username = "John" + " " + "Wick"

print(username)

full_name = first_name + " " + last_name

print(full_name)

# Now create a fourth String variable called:
#
#   suffix
#
# For example, I could declare the variable as:
#
#   suffix = " Jr."
#
# with the space in front being an intentional addition to preserve correct
# appearance of the full name.
#
# Now perform an "in place" assignment, concatenating suffix to your:
#
#   full_name
#
# variable, print the:
#
#   full_name
#
# variable to console again, and run this program via:
#
#   python string_operations.py
#

suffix = " Jr."

full_name = full_name + suffix

print(full_name)