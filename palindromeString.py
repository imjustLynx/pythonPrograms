stringg = str(input("Enter any string: "))
y = ""
for i in stringg:
    y = i + y
if (stringg == y):
    print("String is palindrome")
else:
    print("String is not palindrome")