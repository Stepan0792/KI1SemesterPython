a = float(input("Ваша начальная дистанция в км: "))
b = float(input("Ваша желаемая дистанция в км: "))
i = 1
print(f"{i}: ", "%.2f" % a)
while a < b:
    a = a * 1.1
    i = i + 1
    print(f"{i}: ", "%.2f" % a)

print(f"Ответ: на {i} день спортсмен достиг результата — не менее {b} км")