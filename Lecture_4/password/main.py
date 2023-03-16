# Веб-сайт требует, чтобы пользователи вводили пароль для регистрации, соответствующий определенным требованиям. Напишите программу для проверки правильности ввода пароля пользователями. Ниже приведены критерии проверки пароля:
# 1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
# 2. Минимум 1 число от [0–9]
# 3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
# 4. Минимум 1 специальный символ
# 5. Минимальная длина пароля : 6
# 6. Максимальная длина пароля: 12
# Программа должна возвращать True или False.
# Формат ввода: Passw1#0rd
# Формат вывода: True
s = 'Passw?10rd'


def f(s):
    lett_upp = set('AQWERTYUIOPLKJHGFDSZXCVBNM').intersection(s)
    lett = set('aqwertyuioplkjhgfdsazxcvbnm').intersection(s)
    dec = set('1234567890').intersection(s)
    simb = set('[~!@#$%^&*()_+{}":;\']+$').intersection(s)
    if 5 < len(s) < 13 and lett_upp and lett and dec and simb and not ' ' in s:
        return True
    else:
        return False


print(f(s))