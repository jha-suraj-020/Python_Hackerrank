n = int(input("enter: "))

for i in range(n):
    s = ""
    for j in range(i+1):
        s += chr(96 + n - j) + "-"

    for j in range(i):
        s += chr(96 + n - i + 1 + j) + "-"
    if i == n - 1:
        print(s.center(4 * n - 3, '-')[:(4*n -3)])
    else:
        print(s.center(4 * n - 3, '-'))

for i in range(n-2,-1,-1):
    s= ""
    for j in range(i+1):
        s += chr(96 + n - j) + "-"

    for j in range(i):
        s += chr(96 + n - i + 1 + j) + "-"

    print(s.center(4 * n - 3, '-'))