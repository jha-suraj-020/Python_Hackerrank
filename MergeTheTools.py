#string,k = input("ok: ").split()

string = input("ok ")
k=input()

for i in range(0,len(string),k):
    str = ""
    #mylst = [x for x in string[i:i+k]]
    for letter in string[i:i+k]:
        if letter not in str:
            str += letter

    print(str)



