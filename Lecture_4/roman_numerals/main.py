# Создайте функцию, которая принимает на вход римское число как строку и преобразует ее в целое число, возвращая результат. Функция должна работать для всех римских цифр, представляющих натуральные числа меньше 4000.
# Формат ввода: MMMCMV
# Формат вывода: 3905
s = 'MMMCMV'


def f(s):
    d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    lst = []
    result = 0
    for i in range(len(s)):
        for k, v in d.items():
            if k == s[i]:
                lst.append(int(v))
    for j in range(len(lst)-1):
        if lst[j] < lst[j+1]:
            result -= lst[j]
        else:
            result += lst[j]
    result += lst[-1]    
    return result


print(f(s))
