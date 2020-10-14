n=[1,3,5,6]
t=5
if t in n:
    print(n.index(t))
else:
    n.append(t)
    n.sort()
    print(n.index(t))
