# gyorsabb mint a gyorsítótáras megoldás

fibonacci = (lambda n, a = 0, b = 1 : a if n == 0 else fibonacci(n -1, b, a + b))


for i in range(50):
    print(i , fibonacci(i))
