# Создайте функцию, которая принимает переменное количество аргументов и находит среднее арифметическое ненулевых из них. Обратите внимание на формат вывода
# 1 2 3        --->   2  
# 2 0 0 2 2    --->   2  
# 2 0 2 1 1    --->   1.5
# Формат ввода: 1 2 3 0 0
# Формат вывода: 2
def f(*args):
    s = ' '.join(args)
    n = s.split()
    result = 0
    count = 0
    for j in n:
        if j == '0':
            continue
        else:
            count += 1
    for i in n:
        result += int(i)
    everage = result / count
    if everage % 1 == 0:
        everage = round(everage)
    return everage

print(f('0 20 30'))