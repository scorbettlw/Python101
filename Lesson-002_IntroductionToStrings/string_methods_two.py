"""
    Lesson 002 - Pt7: String Methods II

    Python's ability to manipulate strings is one of the language's
    greatest strengths. The index() and len() methods, when combined
    with Python's slice syntax, makes extracting and/or manipulating
    string methods relatively painless. However, there are a number
    of other important methods that you'll want to know before we move
    on. Let's cover the:

        - replace()
        - find()
        - upper()
        - lower()

    and:

        - capitalize()
    
    methods.

"""

# Let's continue from our last lesson! In addition to extracting strings,
# you can utilize index(), len(), and slice syntax to modify specific substrings.
# For example:
#
#   original_string = "One Two Three"
#
#   search_string = "Three"
#
#   search_string_length = len(search_string)
#
#   search_string_start = original_string.index(search_string)
#
#   original_string[search_string_start:search_string_start + search_string_length] = "Four"
#
#   print(original_string)
#
# Try it out down below. Replace the substring "username" with "user_name", and
# then print the modified string out below.
#

original_string = "full_username"

### CODE HERE: ###


# You've just completed a relatively tricky bit of footwork. Thankfully, there are easier 
# means of replacing a substring within a larger string. Python offers strings a simple,
# elegant method called:
#
#   replace()
# 
# that replaces *all* occurences of the string passed to the method's arguments. Go
# ahead and uncomment the code below and note that we get the exact same result as 
# the previous exercise!
#

# original_string = "full_username"
#
# original_string = original_string.replace("username", "user_name")
#
# print(original_string)
#

# Perfect! As said before, the important thing to remember here is that the
# 
#   replace()
#
# method will replace *all* occurences of the string provided to the method.
# So if we had a string where we only wanted to replace a specific occurence 
# (for example, the first occurence), the previous method of replacing a substring
# is ideal.
#
# Let's try below. Using the:
#
#   replace()
#
# method, replace the duplicate substring " Two" with an empty string "", then
# print the result below:
#

count_string = "One Two Two"

### CODE HERE: ###


# Let's move on to our second method:
#
#   find()
#
# One of the cases we haven't considered is that if index() fails to find the 
# substring passed to it, Python will throw an exception (an error). There are
# plentiful instances where this behavior is undesirable. Rather than simply 
# erroring out, the:
#
#   find()
#
# method returns an integer type value of:
#
#   -1
#
# This is far less disruptive, and when used in tandem with conditional 
# control structures (if/elif/else, we'll get to these soon), is preferable
# and incredibly powerful. Below, call the:
#
#   find()
#
# method on the:
#
#   original_string = "This is my test string."
#
# variable below, passing in the variable:
#
#   query_string = "string"
#
# as the argument, and storing the result in a new variable called:
#
#   starting_index
#
# to be printed below:
#

original_string = "This is my test string."

query_string = "string"

### CODE HERE: ###


# Finally, let's cover three methods that allow you to manipulate the
# capitalization of a string, beginning with:
#
#   upper()
#  
# This method takes a Python string, and returns that string with all
# characters being upper case.  For example, calling:
#
#   upper()
#
# on the string variable below:
#
#   hulk_string = "Hulk angry."
#
# i.e.:
#
#   hulk_string = hulk_string.upper()
#
# and then printing:
#
#   print(hulk_string)
#
# would return:
#
#   "HULK ANGRY."
#
# Let's try it below. Call the:
#
#   upper()
#
# method on the string below, storing that result back in the variable (in-place 
# assignment) and then printing the result. Note that the method takes *no arguments*.
#

store_status = "open"

### CODE HERE: ###


# Of course, if:
#
#    upper()
#
# capitalizes all characters of a string, then the:
#
#   lower()
#
# method makes all characters in a string lower case. Like:
#
#   upper()
#
# the:
#
#   lower()
#
# method takes no arguments. Go ahead and call the:
#
#   lower()
#
# method on the:
#
#   store_status
#   
# variable from above, storing the result back in the variable
# and printing the result.
#

### CODE HERE: ###


# Finally, let's take a look at the:
#
#   capitalize()
#
# method. Where as the:
#
#   upper()
#
# method makes all characters upper case, the:
#
#   capitalize()
#
# method only mutates the first character of a string. For example, while
# calling:
#
#   upper()
#
# on:
#
#   first_name = "John"
#
# would return:
#
#   "JOHN"
#
# calling:
#
#   capitalize()
#
# on:
#
#   first_name
#
# as below:
#
#   first_name.capitalize()
#
# returns:
#
#   "John"
#
# which is what we (more realistically) intend. Try it down below!
# Call:
#
#   capitalize()
# 
# on both the:
#
#   first_name
#
# and:
#
#   last_name
#
# variables, then concatenate these two variables (seperated by a space)
# storing the result in a variable called:
#
#   full_name
#
# and printing:
#
#   full_name
#
# to console.
#

first_name = "Betty"

last_name = "White"

### CODE HERE: ###


