string = input("ok: ")
s1=s2=0
lent = len(string)
for i in range(lent):
    if string[i] in ['A','E','I','O','U']:
        s1 += lent - i
    else:
        s2 += lent - i

if s1 > s2:
    print("Kevin " + str(s1))
elif s1 == s2:
    print("Draw")
else:
    print("Stuart " + str(s2))