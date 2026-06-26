import random

numbers = []

while True:
    num = random.randint(1, 100)  # случайное число от 1 до 100
    numbers.append(num)

    user_input = int(input("Введите число (0 для завершения): "))

    if user_input == 0:
        break

print("Сгенерированные числа:")
for n in numbers:
    print(n)