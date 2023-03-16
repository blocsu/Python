# Для входной строки вычислите символ, который встречается в ней чаще всего.
# Формат ввода: ababaakd30023aaaa
# Формат вывода: a
from collections import Counter
s = 'ababaakd30023aaaa'
foo = Counter(s).most_common(1)
print(foo[0][0])
