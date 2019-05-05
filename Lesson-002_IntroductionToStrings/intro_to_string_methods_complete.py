"""
    Lesson 002 - Pt6: String Operations I

    Now that we've covered operators let's take a look at the:

        - len()

    and:

        - index()

    methods, as well as string indexing and slicing!

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
# One of the most important attributes of a Python string is that it is composed of multiple
# "characters" (individuals letters, numbers, symbols, etc.). Each of these individual characters
# occupies a certain position within a string, and can be accessed using the "slicing" syntax
# available to Python strings (as below):
#
#   example_string = "dog"
#
#   individual_character = example_string[0]
#
# Note that to access an individual character, we need to append a pair of square brackets to the
# end of a string, and then pass the position of the character we want between those brackets. Likewise,
# you'll see above that we've passed the number 0. "Wait", you say, "There isn't 'zero' position though!"
# This is where strings can get a bit tricky. Counter to our intuition, for Python strings, the first
# position is denoted as having an index of zero. That is to say, any valid string that is non-empty 
# (a set of opening and closing quotes like: '' or "" with no other characters between them) starts at
# position zero.
#
# This brings us to an important point. If the first position for a Python string starts at an index of 
# zero, the last character in a string is at an index of the string's length-1. Let's try it below! 
# Access the first and last characters in the string below, storing the first character in a variable 
# named `first_character` and the last character is a variable named `last_character`, and then print 
# those variables below.

my_hero = "Black Widow"

### CODE HERE: ###

# first_character = my_hero[0]

# print(first_character)

# last_character = my_hero[10]

# print(last_character)


# We can pass more than one index at a time of course! Enter Python 'slice' syntax, a means
# of accessing multiple characters between two indicies of a string. An example is below:
#
#   first_name = my_hero[0:5]
#
# Note that a colon (:) seperates the two indices we want to work between. Likewise, it's
# critical to remember that the ending index is not "inclusive". This means that for our example,
# if we want to extract the word "Black" from the string, though the word "Black" occurs between
# indices 0 and 4, we need to start at index 0 and end at index 5. Uncomment and run the code below
# for further proof:

# first_word = my_hero[0:5]

# print(first_word)
#

# Now that we can see that Python strings are just a collection of characters at various positions,
# let's begin with our first method. Much like print, the len() method is built into the Python 
# programming language. The:
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

# favorite_character = "Han Solo"

# character_name_length = len(favorite_character)

# print("String length is:", character_name_length)


# Now that we've covered one of the most important method for strings, let's examine two other
# methods we'll want to use when working with strings. One critical operation you'll run into 
# again and again when working with strings is finding the position of character or smaller 
# string within a larger string. For example, how would we find the starting position of the 
# smaller string:
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
# variable. Be sure to pass the string:
#
#   "dog"
#
# to the method call, store the index in a variable, and print that variable
# to console/shell!
# 

### CODE HERE: ###

# raw_data = "We have two cats, three fish, and a dog."

# start_index = raw_data.index("dog")

# print("Starting index of 'dog':", start_index)


# Using various combinations of index() and len(), we can access almost any part of a string:
# for example:
#
# search_string = "dog"

# search_string_length = len(search_string)

# query_string = "The dog says, 'Woof!'"

# start_position = query_string.index(search_string)

# query_result = query_string[start_position:start_position + search_string_length]

# print(query_result)
#
# This makes extracting substrings incredibly easy! Go ahead and try below. Extract the first
# word in the string below, save it in a new variable, and print the new variable containing the
# first word.
#

my_hero_two = "Ant Man"

### CODE HERE: ###

search_string = "Ant"

search_string_length = len(search_string)

start_position = my_hero_two.index(search_string)

query_result = my_hero_two[start_position:start_position + search_string_length]

print(query_result)


# Next, lets examine a few more methods that are critical to working with strings, the replace,
# find, count, upper, lower, and capitalize methods.
#E