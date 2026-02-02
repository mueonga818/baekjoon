T = int(input())
t = []
for u in range(T):
    t = map(int,input().split())
    t = list(t)
    p = 2 - t[0] + t[1]
    print(p)