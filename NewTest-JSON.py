from itertools import groupby


contents = [
    dict(adult=True, id=111, name="Bob"),
    dict(adult=False, id=332, name="Chris"),
    dict(adult=True, id=113, name="John"),
    dict(adult=False, id=224, name="Amir"),
    dict(adult=True, id=115, name="Yann"),
    dict(adult=False, id=336, name="Lee"),
    dict(adult=False, id=227, name="Nadia"),
    dict(adult=False, id=228, name="Lucy")
]

# XXX: make sure to sort the content list
# with the key you want to group by
contents.sort(key=lambda content: content['adult'])


# then use groupby with the same key
#groups = groupby(contents, lambda content: content['adult'])

#for adult, group in groups:
#    print ('adult', adult)
 #   for content in group:
 #       print ('\t', content)