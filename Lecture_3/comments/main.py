# Большинство сайтов предоставляет возможность оставить комментарий, поэтому необходимо вести их учет, иногда можно увидеть такую запись: Комментарии (28). Давайте составим программу, которая будет записывать слово "комментарий" в нужной форме, например: 
# 24 комментария
# На вход вашей программе подается число, необходимо вывести слово "комментарий" в нужной форме.
def f(n):
    if ((n % 10) == 1 and not 10 < n < 20):
        return str('комментарий')
    elif (2 <= (n % 10) < 5 and not 10 < n < 20):
        return str('комментария')
    elif (10 < n < 20):
        return str('комментариев')
    else:
        return str('комментариев')


n = int(11)
print(f(n))
