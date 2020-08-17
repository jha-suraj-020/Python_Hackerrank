n = int(input())
d = {}

for i in range(n):
    x =input()
    if x not in d.keys():
        d[x] = 1
    else:
        d[x] += 1

print(len(d))
print(" ".join(str(x) for x in d.values()))