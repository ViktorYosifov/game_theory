a = [1, 2, 3]

res = 0

for _ in range(len(a)):
    x = a.pop(0)
    res += sum([j*x for j in a])

print(res)