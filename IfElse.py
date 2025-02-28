a = int(input("Enter age: "))
print(a)

if a <= 0:
    print("Enter a valid age")
elif 0 < a <= 10:
    print("You are a kid")
elif 11 <= a <= 19:
    print("You are a teenager")
elif 20 <= a <= 35:
    print("You are a young adult")
elif 36 <= a <= 60:
    print("You are a middle aged person")
else:
    print("You are a senior citizen")