for i in range(5):
    l = [e for e in range(0,10)]
    print(l)

marks = [65, 71, 68, 74, 61]

# Конвертуємо список в ітератор
iterator_marks = iter(marks)

# Наступний елемент є першим елементом
marks_1 = next(iterator_marks)
print(marks_1)

def check_same_letters(str_obj1: str, str_obj2: str) -> int:
    str_obj1 = str_obj1.lower()
    str_obj2 = str_obj2.lower()
    count = 0

    # Преобразуем строки в множества для получения уникальных букв
    set1 = set(str_obj1)
    set2 = set(str_obj2)

    # Считаем количество уникальных букв из первой строки, которые есть во второй строке
    for el in set1:
        if el in set2:
            count += 1

    print("str1: ", str_obj1)
    print("str2: ", str_obj2)
    print("count: ", count)
    return count

# Проверка функции
check_same_letters("Hilllo", "Hilllo")

