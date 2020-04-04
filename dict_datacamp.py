# from urllib.request import urlopen
# import random
#
# # Load the data from remote location (URL)
# file = urlopen(
#     "https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")
# f = file.read()
#
# # Transform the bitstream into strings
# text = f.decode(encoding='utf-8', errors='ignore')
#
# # Split this single string at the end of lines
# lines = text.split("\n")
#
# # Initalising the dictionary
# reviews = {}
#
# # Filling the dictionary
# for line in lines:
#     l = line.strip().split("\t")
#
#     # These are just training wheels to see more clearly what goes into the dictionary
#     score = l[0]
#     id = l[1]
#     title = l[2]
#     review = l[3]
#
#     reviews[id] = {"score": score, "title": title, "review": review}
#
# # Take a random key from the dictionary and print its value
# print((reviews.items()))
#
# # Counting the number of lines in the file
# print("Number of lines: " + str(len(lines)))
#
# # Counting the keys in the dictionary; should equal the number of lines in the file
# print("Number of dictionary keys: " + str(len(reviews.keys())))
# print(reviews)
# lowscores=[]
# for key,value in reviews.items():
#     if float(value["score"]) == 1.0:
#         lowscores.append(key)
#
# for item in lowscores:
#     print(reviews[item])

# d = {"names":{"name":"Dilip"}, "score":2, "place" : "warangal"}
# print(d.items())
# for key,value in d.items():
#     if value["name"] == "Dilip":
#         print(value["name"])

