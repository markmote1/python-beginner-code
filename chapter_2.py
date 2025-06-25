
''' 1.0 Take definitions.json, read it in as our data, and use a spaced repetition algorithm 
to create a long list where each word is encoutered less and less often, thus increasing the spacing
between encounters as we strengthen our knowledge of the word.'''

# Libraries imports

import json # Importing the json module to read JSON files-it will read the definitions file
import csv #  reading and writing CSV files

'''# 1.1 is to read the definitions file and process it

# 1.2 create a complex object that keeps track of a whole lot of properties about the word or attribute
 / therefore we need to define a class for this object
1.2.1 were going to need to define a bunch of methods(functions specific to a class that are like kind of actions- such as a method, that we can use to automatically handle a word encounter)

  1.3 Instantiate this class/object for every word

  1.4 We can create the spaced repetition algorithms that we'll use to 
  create this long list that clerverly introduces new words, and tests old words at the appropriate 
  intervals

  1.5 save this long list of all our words to a csv file that can later be read by our game
 '''
