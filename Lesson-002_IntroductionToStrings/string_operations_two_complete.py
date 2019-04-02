"""
    Lesson 002 - Pt4: String Operations II

    Now that we've covered the:

        +

    operator (the "concatenation" operator) with respect to Strings,
    let's take a deeper look at concatenation and finally examine another operator.

"""

# The concatenation operator is probably the most common when working with
# Strings. Thusfar though, we've only concatenated two strings at a time. The
# power of the string operator lies in the ability to concatenate three, four, or even
# more strings in a single line of code. Let me demonstrate by example. Let's simplify
# the code from our last program. Create the:
#
#   first_name
#
# and
#
#   last_name
#
# and
#
#   suffix
#
# String-type variables as in our last exercise.
#

### CODE HERE: ###

first_name = "John "

last_name = " Wick"

suffix = " II"


# Now, create the:
#
#   full_name
#
# variable again, but assign the variable as below:
#
#   full_name = first_name + last_name + suffix
#

### CODE HERE: ###

full_name = first_name + last_name + suffix

print(full_name)


# Of course, be sure to print:
#
#   full_name
#
# to console, and then run this program via the command:
#
#   python string_operations_two.py
#

# Switching gears, let's now cover an operator that is perhaps less
# immediately useful than the concatenation operator, but offered to String-type
# data nonetheless. In mathematics, the multiplication operator:
#
# *
#
# is used to denote repeated addition of a numeric value. Again, in Python
# this holds for numeric types like Integers and Floats. For Strings, the multiplication
# operator has the different but useful purpose of repeatedly concatenating the existing
# String data the exact number of times denoted by the integer (whole number) to the right
# of the operator. For example:
#
#   duplicate_first = "John" * 2
#
#   print(duplicate_first)
#
# would output "JohnJohn" to our shell/console. Likewise:
#
#   first_name = "Sam"
#
#   first_name = first_name * 4
#
#   print(first_name)
#
# would output "SamSamSamSam" to our shell/console. Go ahead and create a new variable
# with a good name that represents your favorite onomatopoeia (think Batman's "BAM!"
# or "POW!"). Then perform an "in place" assignment below your declaration, multiplying
# that variable's data by five. For example:
#
#   my_onomatopoeia = "Kablaow!"
#
#   my_onomatopoeia = my_onomatopoeia * 5
#
#   print(my_onomatopoeia)
#

my_onomatopoeia = "Pow!"

my_onomatopoeia = my_onomatopoeia * 5

print(my_onomatopoeia)

### CODE HERE: ###

my_onomatopoeia = my_onomatopoeia * 100

print(my_onomatopoeia)


# As always, be sure to then run this program via:
#
#   python string_operations_two.py
#
# and ask questions in the comments of the video!
#
