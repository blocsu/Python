# Строка считается действительной, если все символы в строке встречаются одинаковое количество раз. Также допустимо, если для выполнения этого условия будет достаточно удалить 1 символ из строки. Напишите функцию, которая возвращает True, если строка действительна и False, если нет.
# abc    ->  True  
# abcc   ->  True
# abccc   ->  Folse
from collections import Counter
s = 'aabbcczzz'


def f(s):
    d = Counter(s)
    lst = d.values()
    d2 = Counter(lst)
    keys = []
    result = 0
    if len(d2) == 1:
        return True
    if len(d2) == 2:
        for v, k in d2.items():
            result = abs(result) - v
            keys.append(k)
        if abs(result) == 1 and  1 in keys:
            return True
        else:
            return False
    else:
        return False


print(f(s))
