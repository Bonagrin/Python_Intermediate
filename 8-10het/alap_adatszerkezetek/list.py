

# Accessing List Elements
a = [10, 20, 30, 40, 50, 10]
print(a[0])     # 10
print(a[-1])    # 50
print(a[1:4])   # 20, 30, 40

# Count
print("Count 10 in list:", a.count(10))

# List with Repeated Elements
a = [2] * 5
b = [0] * 7

print("Repeated Elements", a) # 
print("Repeated Elements", b)


# Adding Elements into List 
a = []

a.append(10) # 1 element
print("After append(10):", a)  

a.insert(0, 5)
print("After insert(0, 5):", a) 

a.extend([15, 20, 25]) # a list to another list
print("After extend([15, 20, 25]):", a) 

numbers = [1, 2, 3] + [4, 5] # extend 2 lists and create a 3rd list(numbers)
print("Add 2 lists elements: ", numbers)

a.clear()
print("After clear():", a)


# Updating Elements into List
a = [10, 20, 30, 40, 50]
a[1] = 25 
print("Update element:", a)


# Removing Elements from List
a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)


# Iterating Over Lists
a = ['apple', 'banana', 'cherry']
print("Iterating over list:")
for item in a:
    print(item)


# Nested Lists
print("Matrix list:")
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])


# List Comprehension
print("List Comprehension")
squares = [x**2 for x in range(1, 6)]
print(squares)


# Copy
a_a = a # same memory area, If a change a_a will change too
a_a = a.copy() # 2 diff memory area, IF a change a_a wont


# Operations
min([3, 2, 5])
max([3, 2, 5])
sum([3, 2, 5]) 
any([True, False, True]) # contains logical true
any([True, True, True]) # check all elements True?


# Sequences
a.sort() # local changes
a_a = sorted(a) # not local changes
a.reverse # local reverse
a_a = reversed(a) # not local reverse
