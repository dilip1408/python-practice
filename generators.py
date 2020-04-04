#Generators takes very less time comparative to lists.
#Generators doesnt holds the entire result in memory, it yields one result at a time. keyword to use generators is "yield".
import time
import math
import timeit
import memory_profiler
import random

# my_nums = (x*x for x in [1,2,3,4,5]) # This is also a generator class
# print(my_nums)
#
# for num in my_nums:
#     print(num)

names = ['Dilip','corey','adam','steve','rick','thomas']

print('memory (Before):{}Mb'.format(memory_profiler.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i, 'names': random.choice(names)
        }
        result.append(person)
    return result

people = people_list(10)

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id':i,'names':random.choice(names)
        }
        yield person
#print(people)


# for items in people:
#     print(items)

t1 = time.process_time()
print(t1)
people = people_generator(1000)
# people = people_list(1000000)
t2 = time.process_time()
print(t2)

print('memory (After):{}Mb'.format(memory_profiler.memory_usage()))
print("Took {} seconds".format(t2-t1))