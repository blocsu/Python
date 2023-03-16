# На вход в программу поступает цвет CSS RGB(A), необходимо определить действителен ли его формат. Создайте функцию, которая принимает строку (например, «rgb (0, 0, 0)») и возвращает True, если формат правильный, в противном случае возвращает False. Данные могут поступать как в формате rgb, так и rgba. Допустимые значения: rgb(0-255, 0-255, 0-255), rgb(0-100%, 0-100%, 0-100%), rgba(0-255, 0-255, 0-255, 0-1)  
# Возможные форматы ввода: 
# rgb(0%,50%,100%) ---> True  
# rgba(0,0,0,0)    ---> True  
# rgb(255,255,255) ---> True  
# rgb(0,,0)        ---> False  
# rgb(-1,0,0)      ---> False  
# rgba(0,0,0,1.5)  ---> False  
# rgba(0,0,0,0.5)  ---> True
# Формат ввода: rgb(-1,0,0)
# Формат вывода: False
import re
s = 'rgb(0%,50%,100%)'


def f(s):
    rgb = re.match(r'rgb\([0-9]+,[0-9]+,[0-9]+\)', s)
    rgb_p = re.match(r'rgb\([0-9]+%,[0-9]+%,[0-9]+%\)', s)
    rgba = re.match(r'rgba\([0-9]+,[0-9]+,[0-9]+,[0-9.]+\)', s)
    result = 0
    lst = []
    if rgb:
        lst = list(s[4:-1].split(','))
        for i in lst:
            if 0 <= int(i) <= 255:
                result += 1
        if result == 3:
            return True
        else:
            return False
    if rgb_p:
        lst = list(s[4:-2].split('%,'))
        for i in lst:
            if 0 <= int(i) <= 100:
                result += 1
        if result == 3:
            return True
        else:
            return False
    if rgba:
        ls = list(s[5:-1].split(','))
        lst = ls[:-1]
        lst_a = float(ls[-1])
        for i in lst:
            if 0 <= int(i) <= 255 and lst_a <= 1:
                result += 1
        if result == 3:
            return True
        else:
            return False
    else:
        return False

      
print(f(s))
