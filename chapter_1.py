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
   # "name" : "mark", 
    "age" : 23, 
    "job" : "developer" }

#boolean- true or false-big part of programming is about logic

True
False

#none- no value-#represents the absence of a value

None

#2.0 VARIABLES - a variable is a label for some data in your program

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


#3.0 LOGIC AND OPERATIONS- operators and functions

#if block - if condition is true execute this code else skip it

if number_of_cats > 2:
    print("too many cats")

print ('We passed the if block')

if 'name' in person:
    print(person['name'])
else:
    print("no name")


if 'milk' in shopping_list:
    print('Need to buy milk')
else:
    print('No need to buy milk')


#Logical operators --- and, or

#if number_of_cats >3:
#    print('we have more than 3 cats')
#    if number_of_cats < 20:
#        print('Yeah, We also have less than 20 cats so the cats no is between 3 - 20')

# This above we can use the 'and' operator

if number_of_cats > 3 and number_of_cats < 20:
    print('we have more than 4 cats so the cats no is between 3 - 20')


if number_of_cats < 5 or number_of_cats >= 20:
    print('Number of cats is outside the range of 4-20')

# Operators

# -Arithmetic operators
# -Assignment operators
# -Comparison operators
# -Logical operators

x = 3
y = 4
print(x * y + x - y / x)

# remainder operator % - it calculates the remainder of a division

remainder = y % x
print(remainder, 10 % 3)

# equality operator == - it checks if two values are equal

print(3 == 3) #true

x == y #false - because x is not equal to y

# not equality operator != - it checks if two values are not equal

print(3 != 3) #false

x != y #true - because x is not equal to y

#same as above
if not number_of_cats == 2:
    print(f'number of cats is not 2 but instead: {number_of_cats}', )

# Loops- while loops and for loops

# -while loop-while this condition is true, keep running this code
count = 0
while count < number_of_cats:
    print( 'Hello world')
    count = count + 2
    if count == 3:
        break



# -for loop-for each item in this list, do this code
for x in shopping_list:
    print(x)


for i in range(10):
    print(i)

length_of_my_array = len(shopping_list)
for j in range(length_of_my_array):
    current_index = j 
    current_value = shopping_list[j]
    print(f'The current index is: {current_index} and the value at that index in the list/array is {current_value}')


