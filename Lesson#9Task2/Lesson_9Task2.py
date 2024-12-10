list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))
numbers = list1 + list2
print("Количество общих чисел:", len(numbers))

