# Создайте программу, которая по почте пользователя, например, user@myserver.com узнает сервер этой почты.
# Формат ввода: ii_ivanov@gmail.com
# Формат вывода: gmail.com
s = str('ii_ivanov@gmail.com')


def x(s):
    i = -1
    result = ''
    while s[i] != '@':
        result = s[i] + result
        i -= 1
    return result


print(x(s))
