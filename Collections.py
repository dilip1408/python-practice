from collections import defaultdict
from operator import itemgetter, attrgetter
'''
# if names used tuples
names = [('mary', 'smith'), ('mark', 'davis')]
# the last_name function would look like
last_name = itemgetter(1)

# if names are dictionaries
names = [{'first': 'mary', 'last':'smith'},{'first': 'mark', 'last': 'davis'}]
# the last_name function would look like
last_name = itemgetter('last')

# if names are classes with first and last as attributes
#names = [Person('mary', 'smith'), Person('mark', 'davis')]
# the last_name function would look like
#last_name = attrgetter('last')

d = defaultdict(list)
for name in names:
	key = last_name(name)
	d[key].append(name)

names = ['mark', 'henry', 'matthew', 'paul',
		 'luke', 'robert', 'joseph', 'carl', 'michael']
# len is our 'key' function here
d = {k: [i for x, i in v]
	 for k, v in itertools.groupby(sorted((len(x), x) for x in names),key=operator.itemgetter(0))}
'''

from collections import defaultdict
res = defaultdict(list)
for v, k in input: res[k].append(v)