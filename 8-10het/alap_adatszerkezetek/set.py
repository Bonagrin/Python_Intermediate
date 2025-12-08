# Create
a = {'one', 'two', "three"}
b = {}

# Empty set
set()

# Immutable set
frozenset([])

# add
a.add('valami')

if 'valami' in a:
    ...
if 'valami' not in a:
    ...
    
# delete
a.remove('valami') # if sure 'valami' is in 
a.discard('valami') # if we not sure 'valami' is in, delete is so
deleted = a.pop() # delete a random element and give back what deleted

# set operations local modifier
a.update({}) # add other set elements, dont duplicate only add the not existing elements

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) 
print(x) # {'apple'}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x) # {'cherry', 'banana'}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) 
print(x) # {'google', 'microsoft', 'banana', 'cherry'}

# new variable, not local modifier
union = a.union(b) 
union = a | b

intersection = a.intersection(b)
intersection = a & b

difference = a.difference(b)
difference = a - b

symmetric_difference = a.symmetric_difference(b)
symmetric_difference = a ^ b


