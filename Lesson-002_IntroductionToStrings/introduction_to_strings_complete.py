"""
    Lesson 002 - Pt2: Introduction to String Variables

    Now that we've reviewed some Python variable basics, let's
    learn a bit about our first data type, Strings! You can think
    of strings as any valid text, like from a book! Strings can contain
    letters, numbers, and characters. Like any data type, strings have
    a number of unique and useful operations available to them you can
    use to change (mutate) the data in string variables, as well as
    a number of built in methods (callable behaviors) that are incredibly
    handy for likewise changing them.


"""


# Let's begin by re-creating our:
#
#   username
#
# variable from the last lesson. Go ahead and (using proper Snake Case)
# re-declare the:
#
#   username
#
# variable below:
#

### CODE HERE: ###

username = "Alan Turing"

print(username)

# If you're lost, get an error, or are otherwise stuck, go ahead and pull up
# the last video and make sure to review the content or ask any questions you
# want answered in the video comments, I'll be glad to help!
#
# If you've been keeping track over the past couple of videos, you'll have
# noticed that any String-type variable's data is surrounded by a set of either
# double or single quotes. For example:
#
#   "David Beckham"
#
# or:
#
#   'David Beckham'
#
# At a base level, either method is fine and roughly equivalent (the differences
# only become important in unique situations that are a topic for an entirely
# different series of videos). However, if you're looking to use a quote as a string,
# for example:
#
# dialogue_one = "She said, "Holy cow!""
#
# or:
#
# statement_one = 'This person's car.'
#
# are not valid. Go ahead and try to run this program with the command:
#
#   python introduction_to_strings.py
#


dialogue_one = 'She said, "Holy cow!"'

statement_one = "This person's car."

print(dialogue_one)

print(statement_one)


# You'll note that the Python interpreter fails to run the program, reporting a Syntax
# Error. The key lesson here is that for a String to be valid, if either a set of
# double-quotes or single-quotes surrounds a string, you *cannot* use that type of
# quote again within that string. So for example, we should change:
#
#   dialogue_one = "She said, "Holy cow!""
#
# to:
#
#   dialogue_one = 'She said, "Holy cow!"'
#
# and:
#
#   statement_one = 'This person's car.'
#
# to:
#
#   statement_one = "This person's car."
#
# Go ahead and make these changes to the incorrect  code above, and then re-run our
# current program via the command:
#
#   python introduction_to_strings.py
#

favorite_food = 'Chocolate Cake'

favorite_song = "Esther's by Amon Tobin"

print("My favorite food is:", favorite_food)

print("My favorite song is:", favorite_song)

