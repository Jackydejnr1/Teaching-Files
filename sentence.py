# Simple Mad Libs game

# Ask the user for different words
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
adverb = input("Enter an adverb: ")

# Create the story using the user's input
story = f"""
Once upon a time, there was a person named {name}.
{name} went to {place}, where they saw a very {adjective} {noun}.
Feeling curious, {name} {verb} {adverb} towards it.
It was a day to remember!
"""

# Display the story
print("\nHere's your story:")
print(story)
