# Напишите программу, которая принимает на вход строку текста и вычисляет количество букв (кириллица, латиница в любом регистре), цифр и специальных символов. При выводе в первой строке указывается количество букв, во второй - количество цифр, в третьей - количество специальных символов.
# Формат ввода: **Hello123**
# Формат вывода:
# 5
# 3
# 4
import re
s = "**Hello123**"
str = re.findall('[a-zA-Zа-яА-Я]', s)
print(len(str))
dec = re.findall('[0-9]', s)
print(len(dec))
simb = re.findall('[^a-zA-Zа-яА-Я0-9_]', s)
print(len(simb))
