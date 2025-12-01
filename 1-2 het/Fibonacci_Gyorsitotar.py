gyorsítótár = [] #cash  

def fibonacci(n):
    if n >=  (méret := len(gyorsítótár)): # méret legyen egyelő := (rozmár operátor)
        gyorsítótár.extend((n + 1 - méret) * [None]) # feltöltöm 10 ig a méretet None val

    if gyorsítótár[n] is not None:
        return gyorsítótár[n] # amelyik értéket ki akarom olvasni és van érték már benne
    
    if n <= 1:
        eredmény = n
    else:
        eredmény = fibonacci(n - 1) + fibonacci(n - 2)

    gyorsítótár[n] = eredmény
    return eredmény

for i in range(50):
    print(i , fibonacci(i))
