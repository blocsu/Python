# Числа Фибоначчи — элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …, в которой первые два числа равны либо 1 и 1, либо 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел. (Википедия) Будем нумеровать числа Фибоначчи начиная с нуля. Получая номер числа Фибоначчи, напечатайте его. ИЗУЧИ РЕКУРСИЮ!!!
# Формат ввода: 8
# Формат вывода: 21
def fib(n, a=0, b=1):
    if (n == 0):
        return a
    else:
        return fib(n - 1, a + b, a)


s = int(6)
print(fib(s))