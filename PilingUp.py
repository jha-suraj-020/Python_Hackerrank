t = int(input())

for z in range(t):
    n = int(input())

    x = None
    list = [int(x) for x in input().split()]

    for i in range(len(list)):

        if list[0] >= list[-1]:
            v = 0
        else:
            v = -1

        if i == 0 or list[v] <= x:
            x = list.pop(v)

        else:
            print("No")
            break
    else:
        print("Yes")