C = int(input())
t = 0
for i in range(C):
    a = list(map(int,input().split()))
    t = 0
    for u in range(a[0]):
        t += a[u+1]
    m = t/a[0]
    c = 0
    for u in range(a[0]):
        if a[u+1] > m :
            c += 1
    rate = c / a[0] * 100
    p = round(rate,3)
    print(p,'%',sep='')