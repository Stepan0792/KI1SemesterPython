a = int(input("Give your number: "))
z = 0
while a > 10:
    b = a % 10
    a = a // 10
    if b > z:
        z = b

print(z)