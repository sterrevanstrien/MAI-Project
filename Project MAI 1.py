#import pandas as pd
#import numpy as np
#import collections

data = open("dialog_acts.dat", "r")
#print(data.read())
 
# Dictionary class
class create_dictionary(dict):
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function which adds key/value pair
  def add(self, key, value):
    self[key] = value
 
# Create two dictionaries, for test and training data.
dict_training = create_dictionary()
dict_test = create_dictionary()

number_of_lines = sum(1 for line in data if line.rstrip())
print('Total lines:', number_of_lines)

# 85% of our data is test data, 15% is training data.
number_training = round((number_of_lines / 100) * 85)
print(number_training)

line_number = 0
for line in data:  # Loop through all lines in data.
    line_number += 1
    
    value, key = line.split(" ", 1)
    if line_number < number_training:   # If it's the first 85% of the input, it's training data. 
        dict_training.add(key, value)
    else:                               # Else it's test data.
        dict_test.add(key, value)
 
#print(dict_data)

# TO DO:
# 1) Test whether the two dictionaries work and start at the right input
# 2) Convert all data to lowercase
# 3) Well we kinda need it to ask for and read input and save it as a variable 'input'
# 4) Next we need it to figure out the majority tag in the data (it's inform, but let's not hard-code it). I guess loop through the training_data dictionary and check which value is most common  
# 5) Create a 'baseline' which always assigns the majority tag, as a tag to any input. This isnt very difficult (or useful, but they want us to make it anyway lol)
# 6) Create a 'baseline' which assigns a tag based on some simple keywords that we pick. Such as 'goodbye' gets tagged as 'bye'. Success rate needs to be 0.8