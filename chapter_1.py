#1.0 DATA TYPES - safe way to store data in a program in a manner that is friendly to python
 #-A data type is a type of data that is friendly to python

# numbers

1234567890

# strings

"mark mote"

#sub-objective-print string

print("mark mote")

# list/array- contain elements of different data types

#uses zero-based indexing-meaning the first element is at index 0
shopping_list = [
    'milk',
    'eggs',
    'bread',
    1,
    []
]


#object / dictionary- contain key-value/definition pairs

person = { 
    "name" : "mark", 
    "age" : 23, 
    "job" : "developer" }

#boolean- true or false-big part of programming is about logic

True
False

#none- no value-#represents the absence of a value

None

#2.0 Variables - a variable is a label for some data in your program

#rules

#-variables cannot start with a number
#-variables can only contain letters, numbers, and underscores-no spaces
#-variables are case-sensitive

number_of_cats = 3 #using snake case-words separated by underscores

my_name = "mark"


print( number_of_cats * 2)

#uses of variables
#-to store data/values
#-to refer to data later in your program and access the values associated with it
#-to make your code more readable
