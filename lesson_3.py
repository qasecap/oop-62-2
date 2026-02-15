# """"""Операторы принадлежности in""""""
# print('p' in 'python')
# print('py' in 'python')
# print('u' in 'python')
#
# print(2 in range(1, 11))
# print(11 in range(1, 11))

# """"""Операторы назначения""""""
# number = 5
# number = number + 3
# number += 3
# number **= 2
# number %= 2
# print(number)
#
# word = 'python'
# word += 'KG'
# word *= 2
# print(word)

# """"""Цикл while""""""
from time import sleep

# counter = 0
# while counter < 100:
#     counter += 1
#     if counter == 72:
#         break
#     if counter in (24, 67, 33, 13):
#         continue
#     print('hello world', counter)

# morning, day, evening = 0, 0, 0

# while True:
#     print(f'у вас {counter} попыток!')
#     time = input('enter time: ').lower().strip()
#     if time in ('morning', 'утро'):

# """"""Цикл for""""""
# i - item, index, iterable

# word = 'KYRGYZSTAN'
#
# for letter in word:
#     print(letter)

# word = 'KYRGYZSTAN'
#
# for letter in word:
#     if letter == 'S':
#         break
#     if letter in 'YR':
#             continue
#     print(letter)

# for number in range(1, 11):
#     if number in (7, 8, 9):
#         print('...')
#         continue
#     print(number)

total_sum = 100
percent = 0.1

for year in range(5):
    total_sum += total_sum * percent
    print(f'Год {year + 1}: {total_sum}')
print(f'Итоговая сумма через 5 лет: {total_sum}')

