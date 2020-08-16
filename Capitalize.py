s = input()
list = s.split(' ')
str = ""

for items in list:
    if items != "" and items[0].isalpha():
        str += items[0].upper() + items[1:]
    else:
        str += items
    str += " "

print(str)