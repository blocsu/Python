# Напишите функцию, которая возвращает самую длинную неповторяющуюся подстроку для входной строки. Если несколько подстрок совпадают по длине, функция возвращает ту, которая встречается первой.
# xxxxx     ->   x  
# abcdefa   ->   abcdef
# Формат ввода: abcabcbb
# Формат вывода: abc
s =  'abcabcbb'


def f(s):
    substr = ''
    lst = []
    all = []
    for obj in list(s):
        if obj not in lst:
            lst.append(obj)
        else:
            all.append(''.join(lst))
            lst.clear()
            lst.append(obj)
    all.append(''.join(lst))
    for j in all:
        if len(j) > len(substr):
            substr = j

    return substr


print(f(s))
