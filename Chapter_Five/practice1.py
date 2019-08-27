#Practice-Dictionary of Words

''' You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. You need to add a few more words and definitions to the dictionary.

After you have added them, use square bracket notation to output the definition of two of the words to the console.

Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.'''

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

word_definitions["transcript"]="A transcript is a document that outlines your academic career."

word_definitions["catalog"]= "The catalog not only outlines the majors, minors, and courses offered, but also contains other important information like your school's history, ethical philosophy, and extra-curricular activities."

word_definitions["prerequisite"]= "The background knowledge needed for your major."

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["credit"]= "A number assigned to each class that measures its level, time commitment, and intensity of the work"

word_definitions["audit"]= "Sitting in a class without receiving a credit for it."

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# print(f"{word_definitions['catalog']}")
# print(f"{word_definitions['transcript']}")

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for key, value in word_definitions.items():
    print(f"The definition of {key} is {value}")
