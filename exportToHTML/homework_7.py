# def nearest_number(numbers, target):
#     sorted_list = sorted(numbers, key=lambda x: abs(x - target))
#     return (target, sorted_list)
# print(nearest_number([312, 996, 31, 1991], 1000))

# числа = [1, 2, 3, 4, 5]
# new_map = list(map(lambda x: x * 10, числа))
# print(new_map)
# new_filter = list(filter(lambda x: x > 3, числа))
# print(new_filter)

# def get_by_index(data=[1, 2, 3, 4, 5]):
#     while True:
#         cmd = input("Введите индекс (или выйти): ")
#
#         if cmd.lower() == "exit":
#             print("До свидания!")
#             break
#
#         try:
#             idx = int(cmd)
#             print(f"Элемент под индексом {idx}: {data[idx]}")
#
#         except ValueError:
#             print("Ошибка! Ввести только цифры.")
#         except IndexError:
#             print(f"Ошибка! В этом списке индексы только от 0 до {len(data) - 1}.")
#
# get_by_index()

# print(100 if 300 // 2 == 150 else 200)

# float("python")

# counter = 5
#
# while counter != 0:
#     print('GEEKS. Python, first month, final test!')
#     counter -= 1

# geeks_in = ["Чуй", "Ыссык-Кол", "Нарын", "Талас", "Джалал-Абад", "Ош", "Баткен"]
#
# geeks_in.sort()
# geeks_in = [i.upper() for i in geeks_in]
#
# geeks_in = geeks_in[::-1]
# print(geeks_in)


клавиши = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х',']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э','z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', 'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж':";", 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.'}
while True:
    user_input = input("введите слово: (Выйти 'q') ").lower()

    if user_input == 'q':
        print("конец")
        break

    result = ""

    for char in user_input:

        if char in клавиши:
            result = result + клавиши[char]
        else:

            result = result + char

    print(result)