# Ввод данных
N = int(input("Введите размер массива N: "))
B = int(input("Введите число B: "))

A = []
for i in range(N):
    A.append(int(input(f"A[{i}] = ")))

count = 0
product = 1

for x in A:
    if x > B:
        count += 1
        product *= x

if count == 0:
    product = 0

print("Количество элементов больше B:", count)
print("Произведение этих элементов:", product)