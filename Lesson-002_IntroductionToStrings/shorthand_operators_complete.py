"""
    Lesson 002 - Pt5: Shorthand Operators

    Thus far we've been using operators and assignments in a very traditional
    fashion. This "longhand" syntax is important, but verbose when all you need
    to do is a quick "in place" reassignment. Let's discuss the shorthand syntax
    for both the concatenation and multiplcation operators and Strings!

"""

# Hopefully you're beginning to feel more comfortable with Strings and the operators
# you've learned. While the syntax we've been using is valid, Python (and many other
# programming languages) often offer a shorthand syntax for quick, "in-place" mutation
# of variables.
#
# The first "shorthand" operator we'll cover is the "in-place" addition operator:
#
#   +=
#
# This just looks like a combination of the addition and assignment operators,
# and that's exactly how it behaves! In the context of the String data type, this
# shorthand operator allows you to concatenate and then reassign the resultant
# concatenation to an existing String-type variable in a single line of code. For
# example:
#
#   username = "George"
#
#   username += " Carlin"
#
#   print(username)
#
# is exactly the same as:
#
#
#   username = "George"
#
#   username = username + " Carlin"
#
#   print(username)
#
# Note that the former is more concise than the latter. There are times where
# you'll want to opt for long form in-place reassignment, particularly when the
# explicitness (obviousness) code is particularly important. The balance between
# concise and explicit code is hotly debated among programmers and developers. Thankfully,
# Python developers are often quick to agree on a proper "Pythonic" way to write code, and
# I encourage you to explore and follow the "Pythonic" way of writing code whenever possible.
#
# Let's go ahead and get some quick practice by using the shorthand addition operator to
# concatenate the String-type variables below! Be sure to print the result to console and
# then run this program via the command:
#
#   python shorthand_operators.py
#


location_name = "San Francisco"

state = ", California"
country = " United States"

### CODE HERE: ###

location_name += (state + country)

print(location_name)


# If you concatenated the variables correctly, "San Francisco, California, United States"
# should print to console.
#

# The multiplication operator has a like shorthand variant:
#
#   *=
#
# that (much like the shorthand addition operator) combines the multiplication and
# assignment operations. The integer value on the right of the operator is first
# used to multiply String-type value contained in the existing variable to the
# right of the operator, and that new value then being reassigned to that existing
# variable.
#
# As before, observe that:
#
#   my_onomatopoeia = "Pow!"
#
#   my_onomatopoeia *= 3
#
#   print(my_onomatopoeia)
#
# is equivalent to:
#
#   my_onomatopoeia = "Pow!"
#
#   my_onomatopoeia = my_onomatopoeia * 3
#
#   print(my_onomatopoeia)
#
# Now go ahead and use the shorthand syntax below to multiply the password variable
# below by six times, then run this program via:
#
#   python shorthand_operators.py
#

password = "shortpass123"

### CODE HERE: ###

password *= 6

print(password)


# As we continue into the numeric types like Integers and Floats, the conciseness of
# shorthand operators will become particularly apparent and important. As always,
# leave a comment in the video if you have any questions!
#
