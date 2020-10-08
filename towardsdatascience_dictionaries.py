# https://towardsdatascience.com/15-things-you-should-know-about-dictionaries-in-python-44c55e75405c
''' 1. What is a Python dictionary?
A dictionary is an unordered and mutable Python container that stores mappings of unique keys to values. Dictionaries are written with curly brackets ({}), including key-value pairs separated by commas (,). A colon (:) separates each key from its value.
Three dictionaries are shown below, containing the population of the 5 largest German cities, list of products, and student’s grades.
'''
# dictionary containing the population of the 5 largest german cities
population = {'Berlin': 3748148, 'Hamburg': 1822445, 'Munich': 1471508, 'Cologne': 1085664, 'Frankfurt': 753056 }

# dictionary containing a list of products' prices
products = {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100}

# dictionary containing students grades
grades = {'Alba': 9.5, 'Eduardo': 10, 'Normando': 3.5, 'Helena': 6.5, 'Claudia': 7.5}

'''
2. Create a dictionary with dict() constructor
Dictionaries can also be created with the built-in function dict(**kwarg). This function takes an arbitrary number of keywords arguments (arguments preceded by an identifier kwarg=value) as input, returning None.
We can also create a dictionary using another dictionary in combination with keyword arguments (dict(mapping, **kwarg)) as follows:
Alternatively, we can construct a dictionary using an iterable (e.g. list of tuples). Each tuple must contain two objects. The first object becomes the key and the second becomes the value of the dictionary.
'''
# create a dictionary with dict() function using keyword arguments # Notice the input was not given in the format of dictionary.. the dict constructor will transform it dictionary format.
# dictionary - ages of students
students_ages = dict(Amanda=27, Teresa=38, Paula=17, Mario=40)

# create a dictionary with dict() function using another dictionary and keyword arguments
# dictionary - ages of students
students_ages = dict({'Amanda':27,'Teresa':38},Paula=18,Mario=40) #Notice the single quotes not given as providing the input to constructor(**kwargs). refer to args&kwargs.py for more details
print(students_ages)

# create a dictionary with dict() function using an iterable (list of tuples). # [] inside dict should be given or else we get error(dict expected at most 1 arguments, got 4) as dict is considering every tuple as a different argument and it expects only one argument.
# dictionary - ages of students
students_ages = dict([('Amanda', 27), ('Teresa', 38), ('Paula', 17), ('Mario', 40)])
print(students_ages)

#Lastly, we can create a dictionary using two lists. First, we have to build an iterator of tuples using zip(*iterables) function. Then, we employ the dict([iterable, **kwarg]) function to construct the dictionary, as we did previously.
students = ['Amanda', 'Teresa', 'Paula', 'Mario']
ages = [27, 38, 17, 40]
s = dict(zip(students,ages))

'''
#Access values in a dictionary
#To access dictionary values, we cannot use a numeric index (as we do with lists or tuples), since the dictionaries are unordered containers. Instead, we enclose the key using square brackets([]). If we try to access a value using an undefined key, a KeyError is raised.
#To avoid getting an exception with undefined keys, we can use the method dict.get(key[, default]). This method returns the value for key if key is in the dictionary, else returns default. If default is not provided, it returns None (but never raises an exception).
'''
# access population
population['Munich']
# 1471508

# # access a value using a numeric index
# population[1]
# # KeyError

# # access population of Stuttgart
# population['Stuttgart']
# # KeyError

# access population of Stuttgart using .get() method without default value
print(population.get('Munich'))
# 1471508

# access population of Stuttgart using .get() method without default value
print(population.get('Stuttgart'))
# None

# access population of Stuttgart using .get() method with default value
print(population.get('Stuttgart', 'Not found'))
# Not found

#Inserting elements
#To insert an element in a dictionary, we can use square brackets as follows:
products['pillow'] = 10
print(products)

#To insert multiple items at once, we can use dict.update([]). This method updates key-value pairs from other,overwriting existing keys.
## add shelf and sofa to the products dictionary using another dictionary object
products.update({'shelf':70,'sofa':300})
print(products)

## add three new items to the grades dictionary using keyword arguments
grades.update(Violeta=5.5, Marco=6.5, Paola=8)
print(grades)

## add two cities to the population dictionary using a list of tuples
population.update([('Stuttgart', 632743),('Dusseldorf', 617280)])
print(population)
#As shown above, the .update() method accepts as an argument not only another dictionary, but also a list of tuples or keyword arguments. This method modifies the dictionary in-place, returning None.


##5. Change elements in a dictionary
#We can change the value of an item by accessing the key using square brackets ([]). To modify multiple values at once, we can use the .update() method, since this function overwrites existing keys.
# Subsequently, we increase the price of a sofa 100 units, and we modify the grades of two students.
print(products)
products['sofa'] = 400

print(products)
#{'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100, 'pillow': 10, 'shelf': 70, 'sofa': 400}

# modify the grades of two students
grades.update({'Normando':2.5,'Violetta':6})
print(grades)

#6. Remove elements in a dictionary
#To remove an element in a dictionary, we can use either the del dict[key] keyword or the dict.pop(key[, default]) method.
#The del dict[key] keyword removes the given element from the dictionary, raising a KeyError if key does not exists.
print(population)
#{'Berlin': 3748148, 'Hamburg': 1822445, 'Munich': 1471508, 'Cologne': 1085664, 'Frankfurt': 753056, 'Stuttgart': 632743,
# 'Dusseldorf': 617280}
# del population['Ingolstadt'] #KeyError: 'Ingolstadt'

# key exists
# the element dusseldorf is removed
del population['Dusseldorf']

# key exists - the item is removed and the value returned
population.pop('Stuttgart')
# 632743 - returned value

#If key exists in the dictionary, the dict.pop(key[, default]) method removes the item with the given key from the dictionary and returns its value. On the contrary, if key does not exist in the dictionary, the method returns the default value. If no default value is provided and key does not exist, the .pop() method will raise an exception (KeyError).

print(population)
#{'Berlin': 3748148, 'Hamburg': 1822445, 'Munich': 1471508, 'Cologne': 1085664, 'Frankfurt': 753056}

# key does not exists but default value is provided
population.pop('Ingolstadt', 'Value not found')
# 'Value not found' - returned value

# # key does not exists and default value is NOT provided
# population.pop('Garching')
# # KeyError

'''
##7. Check if a key exists
# To check whether a key exists in a dictionary, we have to use a membership operator. Membership operators are used to test whether a value is found in a sequence (e.g. strings, lists, tuples, sets, or dictionaries). There are two membership operators, as explained below.
# in → Evaluates to true if the object on the left side is included in the object on the right side.
# not in → Evaluates to true if the object on the left side is not included in the object on the right side.
'''
print('Berlin' in population)
print('Ingolstadt' not in population)
#As shown above, membership operators (in and not in) can be used to check whether a key exists in a dictionary, but they can also be used with other sequences in the following manner.

# membership operators - in / not in
#strings
print('a' in 'Amanda')

#lists
print(3 in [1,2,3,4])

#Tuples
print(s not in (1,2))

#sets
print('Valencia' in {'Barcelona', 'Valencia', 'Madrid','Berlin'})

#8. Copy a dictionary
#To copy a dictionary, we can simply use the dict.copy() method. This method returns a shallow copy of the dictionary. We have to be careful with shallow copies, since if your dictionary contains another container-objects like lists, tuples, or sets, they will be referenced again and not duplicated.

# dictionary with students heights
students = {'Marco': 173, 'Luis': 184, 'Andrea': 168}

# create a shallow copy
students_2 = students.copy()

# modify the height of luis in the shallow copy
students_2['Luis'] = 180

# the modification in students_2 is not observed in students since 180 is an int
print(students)
# {'Marco': 173, 'Luis': 184, 'Andrea': 168}

print(students_2)
# {'Marco': 173, 'Luis': 180, 'Andrea': 168}


# dictionary with students heights and weights
students_weights = {'Marco': [173, 70], 'Luis': [184, 80], 'Andrea': [168, 57]}

# create a shallow copy
students_weights_2 = students_weights.copy()

# modify the height of luis in the shallow copy
students_weights_2['Luis'][0] = 180
# the modification in students_weights_2 is observed in students_weights
# since the list containing the weight and height is referenced and not duplicated
print(students_weights)
# {'Marco': [173, 70], 'Luis': [180, 80], 'Andrea': [168, 57]}

# solution --> create a deepcopy of the dictionary

#To avoid this problem, we can create a deep copy using copy.deepcopy(x) function (defined in the copy module) as follows:

import copy
students_weights_2  = copy.deepcopy(students_weights)
students_weights_2[0] = 174
# the modification in students_weights_2 is NOT observed in students_weights
# since we are working with a deep copy

print(students_weights)
# {'Marco': [173, 70], 'Luis': [184, 80], 'Andrea': [168, 57]}

print(students_weights_2)
# {'Marco': [173, 70], 'Luis': [180, 80], 'Andrea': [168, 57]}

'''
##The difference between shallow copies and deep copies is only relevant when the dictionary contains other objects like lists, since those objects will be referenced instead of duplicated (shallow copy). To create a fully independent clone of the original dictionary, we have to make a deep copy.

#It is important to bear in mind that the = operator does not make a copy of the dictionary. It is just another name to refer to the same dictionary, meaning any modification to the new dictionary is reflected in the original one.
'''

# dictionary with calories in fruits
fruits = {'Orange': 50, 'Apple': 65, 'Avocado': 160, 'Pear': 75}

# copy the dictionary using = operators
fruits_2 = fruits

# modify fruits_2 (delete one item)
fruits_2.pop('Orange')

# the modification is reflected in fruits
print(fruits)
# {'Apple': 65, 'Avocado': 160, 'Pear': 75}

#9. Determine the length of the dictionary
#To determine how many key-value pairs the dictionary contains, we can use the len() function. This function returns the number of items of an object. The input of the function can be a dictionary, but also another type of sequence such as a string, list, tuple, or set.

print(population)
print(len(population))

#10. Loop through a dictionary
#Iterating through keys
#To iterate over the keys, we can use the dictionary directly in a for loop as follows:

# iterate through keys
for city in population:
    print(city)

#Alternatively, we can use the dict.keys() method. This method returns a view object, containing the keys of the dictionary.
for city in population.keys():
    print(city)
'''
#Iterating through values
#If you just need to work with the values of a dictionary, then you can use the dict.values() method in a for loop. This method returns a view object that contains the values of the dictionary.
'''
#We can compute how many people live in the 5 largest German cities using dict.values() method as follows:

inhabitants=0
for number in population.values():
    inhabitants += number
print(inhabitants)

'''
#Iterating through items
#When you’re working with dictionaries, it’s likely that you need to use the keys and the values. To loop through both, you can use the dict.items() method. This method returns a view object, containing key-value pairs as a list of tuples.
#We can determine the student with the lowest test score using the dict.items() method in combination with a for loop as follows:
'''

# students grades dictionary
print(grades)
# {'Alba': 9.5, 'Eduardo': 10, 'Normando': 2.5, 'Helena': 6.5, 'Claudia': 7.5, 'Violeta': 6, 'Marco': 6.5, 'Paola': 8}

# dict.items() - dictionary view object containing key-value pairs as a list of tuples
grades.items()
# dict_items([('Alba', 9.5), ('Eduardo', 10), ('Normando', 2.5), ('Helena', 6.5), ('Claudia', 7.5),
#             ('Violeta', 6), ('Marco', 6.5), ('Paola', 8)])

# determine student with the lowest test score
min_grade = 10
min_student = ''
for student, grade in grades.items():
    if grade < min_grade:
        min_student = student
        min_grade = grade

print("LOwest test score",min_student)
# Normando

'''
#11. Dictionary comprehensions
Python for-loops are very handy in dealing with repetitive programming tasks; however, there is another alternative to achieve the same results in a more efficient way: dictionary comprehensions.
Dictionary comprehensions allow the creation of a dictionary using an elegant and simple syntax: {key: value for vars in iterable}. In addition, they are faster than traditional for-loops.
We can filter the products with a price lower than 100 euros using both a traditional for-loop and a dictionary comprehension. '''

# list of prices
print(products)
# {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100, 'pillow': 10, 'shelf': 70, 'sofa': 400}

##########################
###traditional for loop###
##########################

# empty dictionary
products_low = {}

# select only the items with a price lower than 100
for product, value in products.items():
    if value < 100:
        products_low.update({product: value})

print(products_low)
# {'chair': 40, 'lamp': 14, 'pillow': 10, 'shelf': 70}


##############################
###dictionary comprehension###
##############################

# select only the items with a price lower than 100
products_low = {product: value for product, value in products.items() if value < 100}

print(products_low)
# {'chair': 40, 'lamp': 14, 'pillow': 10, 'shelf': 70}
#As we can observe, dictionary comprehensions provide the same results as traditional for-loops in a more elegant way.

'''
12. Nested dictionaries
Nested dictionaries are dictionaries that contain other dictionaries. We can create a nested dictionary in the same way we create a normal dictionary using curly brackets ({}).
The following nested dictionary contains information about 5 famous works of art. As we can observe, the values of the dictionary are other dictionaries as well.
'''
# nested dictionary containing information about famous works of art
works_of_art = {'The_Starry_Night': {'author': 'Van Gogh', 'year': 1889, 'style': 'post-impressionist'},
                'The_Birth_of_Venus': {'author': 'Sandro Botticelli', 'year': 1480, 'style': 'renaissance'},
                'Guernica': {'author': 'Pablo Picasso', 'year': 1937, 'style': 'cubist'},
                'American_Gothic': {'author': 'Grant Wood', 'year': 1930, 'style': 'regionalism'},
                'The_Kiss': {'author': 'Gustav Klimt', 'year': 1908, 'style': 'art nouveau'}}
print(works_of_art)
#To access elements in a nested dictionary, we specify the keys using multiple square brackets ([]).
# access elements in a nested dictionary
works_of_art['Guernica']['author']
# 'Pablo Picasso'

works_of_art['American_Gothic']['style']
# 'regionalism'

#13. Alternative containers : OrderedDict, defaultdict, and Counter
'''
The collections module provides alternative container datatypes to built-in Python containers. Three dictionary subclasses contained in the collections module that are pretty handy when working with Python are: (1)OrderedDict, (2)defaultdict, and (3)Counter.
OrderedDict
OrderedDict consists of a dictionary that remembers the order in which its contents are added. In Python 3.6+ dictionaries are also insertion ordered, meaning they remember the order of items inserted. However, to guarantee element order across other Python versions, we have to use OrderedDict containers.
'''

import collections

# create an OrderedDict of chemical elements
dictionary = collections.OrderedDict({'hydrogen': 1, 'helium': 2, 'carbon': 6, 'oxygen': 8})

# type OrderedDict
print(type(dictionary))
# <class 'collections.OrderedDict'>

# dictionary keys --> .keys() method
print(dictionary.keys())
# odict_keys(['hydrogen', 'helium', 'carbon', 'oxygen'])

# dictionary values --> .values() method
print(dictionary.values())
# odict_values([1, 2, 6, 8])

# insert a new element
dictionary['nitrogen'] = 7

# nitrogen last position since it is the last element added
print(dictionary)
# OrderedDict([('hydrogen', 1), ('helium', 2), ('carbon', 6), ('oxygen', 8), ('nitrogen', 7)])
#As shown above, OrderedDict accepts dictionary methods and functions. Moreover, elements can be inserted, changed, or deleted in the same way as with normal dictionaries.

import collections

# create an OrderedDict of chemical elements
dictionary = collections.OrderedDict({'hydrogen': 1, 'helium': 2, 'carbon': 6, 'oxygen': 8})

# type OrderedDict
print(type(dictionary))
# <class 'collections.OrderedDict'>

# dictionary keys --> .keys() method
print(dictionary.keys())
# odict_keys(['hydrogen', 'helium', 'carbon', 'oxygen'])

# dictionary values --> .values() method
print(dictionary.values())
# odict_values([1, 2, 6, 8])

# insert a new element
dictionary['nitrogen'] = 7

# nitrogen last position since it is the last element added
print(dictionary)
# OrderedDict([('hydrogen', 1), ('helium', 2), ('carbon', 6), ('oxygen', 8), ('nitrogen', 7)])

#As shown above, OrderedDict accepts dictionary methods and functions. Moreover, elements can be inserted, changed, or deleted in the same way as with normal dictionaries.

#defaultdict
#Defaultdicts are a dictionary subclass that assign a default value when a key is missing (it has not been set yet). They never raise a KeyError, if we try to access an item that is not available in the dictionary, instead a new entry is created.
#Defaultdicts take a function as an argument, and initialize the missing key with the value returned by the function. In the example below, the keys are initialized with different values, depending on the function employed as first argument.


import collections
import numpy as np

# missing key initialized with a 0
default_1 = collections.defaultdict(int)

default_1['missing_entry']
print(default_1)
# defaultdict(<class 'int'>, {'missing_entry': 0})

# missing key initialized with an empty list
default_2 = collections.defaultdict(list, {'a': 1, 'b': 2})

default_2['missing_entry']
print(default_2)
# defaultdict(<class 'list'>, {'a': 1, 'b': 2, 'missing_entry': []})

# missing key initialized with a string
default_3 = collections.defaultdict(lambda : 'Not given', a=1, b=2)

default_3['missing_entry']
print(default_3)
# defaultdict(<function <lambda> at 0x000001DEF6ADF730>, {'a': 1, 'b': 2, 'missing_entry': 'Not given'})

# missing key initialized with a numpy array
default_4 = collections.defaultdict(lambda: np.zeros(2))

default_4['missing_entry']
print(default_4)
# defaultdict(<function <lambda> at 0x000001DEF6ADF950>, {'missing_entry': array([0., 0.])})
#As we can observe, we can pass a dictionary or keywords as second argument (optional) to initialize the defaultdict container.


#Counter
#A Counter is a dictionary subclass for counting hastable objects. The function returns a Counter object, where elements are stored as keys and their counts are stored as values. Using this function, we can easily count the elements of a list, as shown below.

letters = ['a','b','c','a','b','e','d']

counter = collections.Counter(letters)
print(counter)
print(counter.most_common(3))
#As shown above, we can easily obtain the most frequent elements with the .most_common([n]) method. This method returns a list of the n most common elements and their counts.

#14. Create a Pandas DataFrame from a dictionary.
#A Pandas DataFrame is a two-dimensional tabular data where each row represents an observation and each column a variable. A Pandas DataFrame can be created using the pandas.DataFrame constructor. This function accepts as input various python containers (e.g. lists, dictionaries, or numpy arrays). However, in this article, we explain only the ways to create a DataFrame that involve the use of dictionaries.
#Create a DataFrame from a dictionary
#We can create a DataFrame from a dictionary, where the keys represent column names, and the values represent column data in the following manner:

import pandas as pd

# create a Pandas DataFrame from a dictionary - keys (column name) - value (column data)
df = pd.DataFrame({'name': ['Mario', 'Violeta', 'Paula'],
                     'age': [22, 27, 19],
                     'grades': [9, 8.5, 7]})
print(df)
#As we can observe, the default index is just the row number (an integer index beginning at 0). We can modify these indexes by passing the index list to the DataFrame constructor.

df_index = pd.DataFrame({'name': ['Mario', 'Violeta', 'Paula'],
                     'age': [22, 27, 19],
                     'grades': [9, 8.5, 7]}, index=['student_1','student_2','student_3'])

print(df_index)

#Create a DataFrame from a list of dictionaries
#A list of dictionaries can also be used to create a DataFrame, where the keys represent column names. As before, we can change indexes by passing the index list to the DataFrame function.
# create a Pandas DataFrame from a list of dictionaries - keys(column name) - with custom indexes
df_2 = pd.DataFrame([{'name': 'Mario', 'age': 22, 'grades':9},
                     {'name': 'Violeta', 'age': 27, 'grades':8.5},
                     {'name': 'Paula', 'age': 19, 'grades':7}], index=['student_1', 'student_2', 'student_3'])

print(df_2)