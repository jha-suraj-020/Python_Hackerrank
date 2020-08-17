list = [1,2,3,4,2,3,5,5,5]

for i in list:
    cnt = list.count(i)
    if cnt > 1:
        for j in range(cnt - 1):
            list.remove(i)

list.sort()
list.reverse()
print(list)
