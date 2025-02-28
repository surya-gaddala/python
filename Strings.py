str= "Surya"
print(str)

name = 'surya'
# print(name)
# print(name[0])
# print(name[1])  
# print(name[2])
# print(name[3])
# print(name[4])
print(name[5:0])
for char in name:
    print(char)

names = "surya,Raj"
print(names.split(','))

title ="my name is surya"
title.split(" ")
reversed_title = ""
for char in title:
    reversed_title = char + reversed_title
print(reversed_title)  