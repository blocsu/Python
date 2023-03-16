# Для строки вывести статистику по количеству входящих в нее символов (без учета регистра), сортируя по алфавиту. Игнорируйте всё, кроме букв латиницы и кириллицы. Вывод: символ, пробел, количество. Приоритет вывода у латиницы, вывод символов в нижнем регистре.
# Формат ввода: Hello 123 ** hello мама
# Формат вывода:
# e 2
# h 2
# l 4
# o 2
# а 2
# м 2
from collections import Counter
import re
str = 'Hello 123 ** hello мама'
s = str.lower()
filt = re.sub(r'[0-9 \t\s(+*\d.\W)]', '', s)
c = Counter(filt).most_common()
sort = sorted(c)


def f(sort):
    for key, value in sort:
        print(key, value)
    return


f(sort)
