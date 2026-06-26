n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    element = int(input(f"Введите элемент A[{i}]: "))
    a.append(element)

sum_positive = 0
count_positive = 0

for i in range(n):
    if a[i] > 0:
        sum_positive += a[i]
        count_positive += 1

print("Сумма положительных элементов:", sum_positive)
print("Количество положительных элементов:", count_positive)