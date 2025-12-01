def fun(m):
    for i in range(m):
        yield i  

# call the generator function
for n in fun(5):
    print(n)