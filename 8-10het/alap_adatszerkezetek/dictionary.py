
# create
dictionary = {'a' : 'aa', 'b' : 'bb'}

# empty
dictionary = {}
 
dictionary = dict()

# get, get back the value of the key
dictionary.get('a')
dictionary['a']

# add
dictionary['a'] = 'aa'

# modify
dictionary['a'] = 'ab'
dictionary.update({'a': 'aa', 'b': 'bb'})

# delete
deleted = dictionary.pop('a')


# check process, values are True or False
if 'a' in dictionary:
    ... 
if 'a' not in dictionary:
    ...

# dyct create from list
list1 = []
list2 = []
dictionary = dict(zip(list1, list2))

# dict comprehension
value = {i : i*i for i in range(10)}

# print key value
dictionary.keys()
dictionary.values()
dictionary.items()

# sort by values
dict(sorted(dictionary.items(), key = lambda value: value[1]))
 


