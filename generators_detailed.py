# link - https://realpython.com/introduction-to-python-generators/
# def csv_reader(file_name,state):
#     try:
#         for row in open(file_name, state):
#             yield row
#     except FileNotFoundError:
#         exit(1)
#
# # csv_reader("C:/Users/dvoruga/Downloads/techcrunch.txt",'r')
# import time
# # start = time.time()
# csv_reader = (row for row in open("C:/Users/dvoruga/Downloads/techcrunch.txt",'r'))
# count = 0
#
# # print(start)
#
# for now in csv_reader:
#     count += 1
# # print(time.time() - start)
# print(count)

# def infinite_sequence():
#     num = 0
#     while True:
#         num += 1
#         yield num
#
# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
#############################

# #Profiling---- memory utilized by regular function vs generator----
# import sys
# func = [n*2 for n in range(10000)]
# gen = (n*2 for n in range(10000))
#
# print(sys.getsizeof((func))) #-- 87624 bytes
# print(sys.getsizeof((gen))) # -- 120 bytes
#############################

# #---  list comprehensions can be faster to evaluate, but memory efficient is generators --
# #There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory, then list comprehensions can be faster to evaluate than the equivalent generator expression. To explore this, let’s sum across the results from the two comprehensions above. You can generate a readout with cProfile.run():
#
# import cProfile
# cProfile.run('sum([n*2 for n in range(10000)])')
# cProfile.run('sum((n*2 for n in range(10000)))')
#
# #Here, you can see that summing across all values in the list comprehension took about a third of the time as summing across the generator. If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.
#######################

# #--implement your own for loop by using a while loop---
# # StopIteration is a natural exception that’s raised to signal the end of an iterator. for loops, for example, are built around StopIteration. You can even implement your own for loop by using a while loop:
#
# vowels = ['a','e','i','o','u']
# vowels = iter(vowels)
# while True:
#     try:
#         print(next(vowels))
#     except StopIteration:
#         break
# ###############################

### _ palindrome number or not#####
# def is_palindrome(num):
#
#     # num = 122
#     if (num//10 == 0):
#         pass
#     temp = num
#     reversed_no = 0
#
#     while(temp != 0):
#         reversed_no = (reversed_no * 10)
#         reversed_no1 = reversed_no + (temp % 10)
#         print(reversed_no1,"::::::::::")
#         temp = temp // 10
#     if(num == reversed_no1):
#         # return num
#         print(num, "is a palindrome")
#     else:
#         print(num,  "is  NOT a palindrome")
#
# a = is_palindrome(122)
# print(a)
#
# #####################################
import sys
file_name = "C:/Users/dvoruga/Downloads/techcrunch.csv"
lines =(line for line in open(file_name))
list_line = (s.strip().split(",") for s in lines)
print(sys.getsizeof(list_line))
cols = next(list_line)
company_dicts = (dict(zip(cols,data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
print(funding)
total_series_a = sum(funding)
print(total_series_a)




# lines = (line for line in open(file_name))
# print(lines)

# li = (li.rstrip().split(",") for li in lines)
# print()
# print(li)
# cols = next(li)
# print(cols)
# dictionary = (dict(zip(cols, data)) for data in li)

# print((dictionary[0]['round']))

# funding = [int(dicts["raisedAmt"]) for dicts in dictionary if dicts["round"] == "a"]
# print(sum(funding))



# def funding():
#     total_amt = 0
#     length = 0
#     for count,dicts in enumerate(dictionary,1):
#         # print(count, dicts)
#
#         if dicts["round"] == "d":
#             print((dicts["raisedAmt"]), count, length)
#             total_amt += int(dicts["raisedAmt"])
#             length += 1
#
#     return total_amt, count, length


# print(funding())
# print(type(funding),len(funding),sum(funding))
# print(sum(funding)/len(funding))
# # funding = ( int()for dicts in dictionary)
# # print(sum(funding))

#------------------To get size of variable and how open functionality works in terms of memory --------
# import sys
# # lines = open("C:/Users/dvoruga/Desktop/techcrunch.csv") # This file consists of less number of lines  when comared to below line but still memory utilized is same for both the files.
# lines = open("C:/Users/dvoruga/Downloads/techcrunch_doubleRows.csv") # consists of 2921 lines
# count = 0
# for line in lines:
#     count += 1
# print(count)
# print(sys.getsizeof(lines))