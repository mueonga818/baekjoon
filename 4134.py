def  prime (x):
    p = 0
    for i in range(1, x+1):
        if x%i ==  0:
            p += 1
    if p == 2:
        return (True)
    else:
        return (False)
T = int(input())
for t in range(T):
    p = []
    n = int(input())
    i = n//2
    u = n-i
    while 1 == 1:
        if prime(i) == True and prime(u) == True:
            p = (i, u)
            break
        i += 1
        u = n-i
    print(min(p), max(p))