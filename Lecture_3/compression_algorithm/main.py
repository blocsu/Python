# Написать программу для сжатия строки, в которой алгоритм работает следующим образом: string = 'xxxxtttсyyaaa' преобразуется в 'x4t3с1y2a3', то есть последовательность одинаковых символов строки заменяется на этот символ и количество его повторений в текущей позиции строки.
# Формат ввода: xxxxtttсyyaaa
# Формат вывода: x4t3с1y2a3
s = 'xxxxtttсyyaaaxxxx'


def f(s):
    i = s[0]
    count = 0
    result = ''
    for obj in s:
        if obj == i:
            count += 1
        else:
            result += i + str(count)
            count = 1
            i = obj
    result += i + str(count)
    return result


print(f(s))