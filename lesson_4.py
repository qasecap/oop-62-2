# """"""Добавление""""""
# numbers = [21, 32, 13, 4, 15]
# print(numbers)
# numbers.append(6)
# numbers.insert(0, 0.5)
# numbers.extend( 7, 8, 9)

# """"""Редактирование""""""
# numbers.reverse()
# numbers.soft(reverse=True)
# numbers[1] = 99
# numbers[2:4] = [5, 6]
#
# print(numbers)

# # """"""Управление""""""
# deleted = numbers.pop(0)
# numbers.remove(4)
# del numbers[-2:]
# numbers.clear()
#
# print(numbers)
# print(deleted)

# """"""Встроенные функции к наборам элементов""""""
# numbers = [21, 32, 13, 4, 15]
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# """"""Список включения List comprehension. [объект, цикл, условие]""""""
cities = ['tokmok', 'kemin', 'bishkek', 'karakol', 'kant']
print(cities)

# cities_new = [city.title() for city in cities if city.startswith('k')]
cities_new = [city.title() for city in cities if 'i' in city]
print(cities_new)