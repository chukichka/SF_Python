def binary_search(array, element, left, right):
    middle = (right + left) // 2  # находимо середину

    if array[middle] <= element:  # если элемент больше или равен середине
        if array[middle + 1] < element: # если следующее после середины число меньше введенного элемента
            return binary_search(array, element, middle + 1, right) # в рекурсии продолжается поиск по правой части
        elif array[middle] == element: # если элемент уже есть в списке
            return f"Элемент с индексом {middle - 1} предшествует {element}."
            # СТРОКА ДЛЯ ПРОВЕРКИ: значит выводится предшествующее элементу число и его индекс, а также последующее число, которое равно элемента
            # return f'Элементу {element} предшествует элемент {array[middle - 1]} с индексом {middle - 1}.\n' \
            #        f'Последующий элемент {array[middle]} с индексом {middle} равен {element}.'
        else:
            return f"Элемент с индексом {middle} предшествует введенному элементу {element}."
            # СТРОКА ДЛЯ ПРОВЕРКИ: значит выводится предшествующее элементу число и его индекс, а также последующее число, которое больше элемента
            # return f'Элементу {element} предшествует элемент {array[middle]} с индексом {middle}.\n' \
            #        f'Последующий элемент {array[middle+1]} больше {element}.'

    elif element < array[middle]: # если элемент меньше середины
        return binary_search(array, element, left, middle - 1) # в рекурсии продолжается поиск по левой части

# Тестовая последовательность: 26 12 37 9 6 0 -7 11 58 96 69 147 88 23
num_array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
num = int(input("Введите любое целое число: "))
num_array = sorted(num_array) # сортировка списка

for i in num_array:
    # проверка, что введенное число не больше максимального элемента в списке, и
    # проверка, что введенное число не меньше минимального элемента или не равно ему
    if (i < num and num_array.index(i) == len(num_array) - 1) or \
            (i >= num and num_array.index(i) == 0):
        print(f"По введенным данным невозможно произвести поиск. Перезапустите программу.")
        raise ValueError

print(binary_search(num_array, num, 0, len(num_array) - 1))
# СТРОКА ДЛЯ ПРОВЕРКИ: отображает отсортированный список, по которому можно проверить
# print("Отсортированный список: ", num_array)
