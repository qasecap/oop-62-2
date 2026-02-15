while True:
    word = input('Введите слово: ')
    if word == 'Выход':
        break

    count_total = 0
    count_vowels = 0
    count_consonants = 0

    vowels = 'aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ'

    for letter in word:
        count_total += 1
        if letter in vowels:
            count_vowels += 1
    else:
        count_consonants += 1

    print('Количество букв:', count_total)
    print('Гласных букв:', count_vowels)
    print('Согласных букв:', count_consonants)

    percent_vowels = count_vowels / count_total * 100
    percent_consonants = count_consonants / count_total * 100
    print(f'Гласные/Согласные: {percent_vowels:.1f}% / {percent_consonants:.2f}%')