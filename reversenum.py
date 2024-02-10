num = int(input("Enter a number: "))
reverseNum = 0

while num != 0:
    digit = num % 10
    reverseNum = reverseNum * 10 + digit
    num //= 10

print("Reversed Number: ", reverseNum)