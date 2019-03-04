"""
    Lesson 002 - Pt6: Introduction to String Methods

    We've already been using the:

        print()

    method (recall, a method is like a callable behavior or action), which is built-in to
    Python and allows us to display the data in our variables. Did you know that Python
    strings have a massive suite of like, helpful methods we can use to manipulate them?
    Here, we'll cover a handful of essential methods you need to know when working with
    strings in Python while diving deeper into what methods really are and represent
    in an object-oriented programming language.

"""

# As Python strings can be manipulated via the addition (concatenation) operator
# and the multiplication operator, it might be a surprise that neither the subtraction
# or division operator are available to this data type. While at first confusing, when
# stop and think for a second it make sense. How would subtracting or "dividing" two
# strings even work? For some, a likely answer for the former might be "replacing or
# removing characters or text in a string", however the logistics of how a subtraction
# operator would handle mismatches or partial matches in replacing text seems to warrant
# a more explicit approach.
#
# This is where methods built in. If primitive data types are like fundamental Lego
# building blocks, then you can think of methods as common operations or actions you'd like
# to easily call and use when building with that particular brick type. More formally,
# methods are *functions* (we'll cover these later), repeatable and callable behaviors,
# associated with a particular data type. Most methods directly manipulate the data of the
# variable upon which they are called, although some exist solely to provide additional,
# useful information about a given variable of a certain data type.
#
# Let's begin with another method that, much like print, is built into the Python programming
# language. The:
#
#   len()
#
# method can be called and passed any valid string data, and returns the length (number of
# characters) in that string. Note that unlike print, which will output information regarding
# almost any data type to console, the:
#
#   len()
#
# method can only be passed valid string-type data. For example:
#
#   print(len("Happy"))
#
# will output 5 to console/shell. Likewise:
#
#   mood = "sad"
#
#   mood_length = len(mood)
#
#   print(mood_length)
#
# will output 3 to console/shell. However, if we try to run:
#
#   print(len(5))
#
# or
#
#   mood = "sad"
#
#   mood_length = len(mood)
#
#   print(len(mood_length))
#
# the Python interpreter will output an error. This isn't to say you can't find the number of
# digits in a number, this just isn't the method for it!
#
#
# Let's give it a shot! Create a variable containing your favorite TV/Movie character's name,
# (string-type, obviously). Call the:
#
#   len()
#
# method on the variable and story the result in a variable called:
#
#   character_name_length
#
# and then print both the character name and character name length to console/shell. Be sure to
# run this program via the command:
#
#   python intro_to_string_methods.py
#

### CODE HERE: ###


# Now that we've covered arguably the most important method for strings, let's examine two other
# important behaviors we might want to use when working with strings. One critical operation
# you'll run into again and again when working with strings is finding the position of character
# or smaller string within a larger string. For example, how would we find the starting position
# of the smaller string:
#
#   "dog"
#
# within the larger string:
#
#   "type: dog"
#
# A casual Google search will result in a confusing mass of developers arguing over best practices,
# talk of algorithms, and debate over theoretical run times. While these are important topics,
# we're simply looking for the built-in solution Python offers, of which there are two.
#
# The first method is:
#
#   index()
#
# which can be called upon a string as below:
#
#   print("type: dog".index("dog"))
#
# or a variable containing a valid string as below:
#
#   raw_dog_data = "type: dog"
#
#   dog_index = raw_dog_data.index("dog")
#
#   print(dog_index)
#
# either of which while output 6 to console/shell. Note that unlike the:
#
#   len()
#
# method, we call the:
#
#   index()
#
# method on the string or variable (containing a string) we want to search, and pass the
# method the string we want to find the starting position of. This structure of calling
# a method upon the instance of data we want to mutate or extract additional information from
# while passing required, additional information to the called method how the majority of methods
# are called on both Python data types and data types of other programming languages in general.
#
# Go ahead and complete the code below by adding a line which calls the index() method
# on the:
#
#   raw_data
#
# variable. Be sure to pass the
#
#
