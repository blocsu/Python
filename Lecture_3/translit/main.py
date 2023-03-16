# Написать программу для транслитерации фамилии, имени, отчества для загранпаспорта по установленным МВД РФ требованиям:
# А (а) -> A (a)   Ж (ж) -> Zh (zh)    Н (н) -> N (n)   Ф (ф) -> F (f)        Ъ (ъ) -> Ie (ie) Б (б) -> B (b)   З (з) -> Z (z)      О (о) -> O (o)   Х (х) -> Kh (kh)      Э (э) -> E (e) В (в) -> V (v)   И (и) -> I (i)      П (п) -> P (p)   Ц (ц) -> Ts (ts)      Ю (ю) -> Iu (iu) Г (г) -> G (g)   Й (й) -> I (i)      Р (р) -> R (r)   Ч (ч) -> Ch (ch)      Я (я) -> Ia (ia) Д (д) -> D (d)   К (к) -> K (k)      С (с) -> S (s)   Ш (ш) -> Sh (sh)      ь     -> не пишется 
# Е (е) -> E (e)   Л (л) -> L (l)      Т (т) -> T (t)   Щ (щ) -> Shch (shch)  
# Ё (ё) -> E (e)   М (м) -> M (m)      У (у) -> U (u)   Ы (ы) -> Y (y)
# Формат ввода: Попов Василий Вячеславович
# Формат вывода: Popov Vasilii Viacheslavovich

s = 'Доценко Полина Евгеньевна'


def translit(s):
    cyrillic1 = ' абвгдеёжзийклмнопрстуф'
    cyrillic2 = 'хцчшщъыьэюяАБВГДЕЁЖЗИЙК'
    cyrillic3 = 'ЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin1 = ' |a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f'
    latin2 = '|kh|ts|ch|sh|shch|ie|y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I|K'
    latin3 = '|L|M|N|O|P|R|S|T|U|F|Kh|Ts|Ch|Sh|Shch|Ie|Y||E|Iu|Ia'
    cyrillic = cyrillic1 + cyrillic2 + cyrillic3
    latin = (latin1 + latin2 + latin3).split('|')
    d = dict(zip(cyrillic, latin))
    str = ''
    for i in range(len(s)):
        for key, value in d.items():
            if key == s[i]:
                str += value
    return str


print(translit(s))
