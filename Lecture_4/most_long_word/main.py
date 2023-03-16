# Напишите функцию, которая будет возвращать самое длинное слово в предложении. Если найдено более одного слова, то функция возвращает первое.
# Формат ввода: The Tower of London was built in the 15th century
# Формат вывода: century
s =  'The Tower of London was built in seventh the 15th century'


def f(s):
    lst = s.split()
    result = ''
    for i in lst:
        if len(i) > len(result):
            result = i
    return result



print(f(s))
