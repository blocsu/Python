from urllib.request import urlopen
import xml.etree.ElementTree as ET
tree = ET.parse(urlopen('http://www.cbr.ru/scripts/XML_daily.asp'))
# Определяем родительский элемент в дереве XML
root = tree.getroot()
# Находим и перебираем все елеменыт 'Valute' в общем дереве
for child in root.findall("Valute"):
    # Находим в полученых элементах содержимое элементов Name и Value
    print(f'{child.find("Name").text} {child.find("Value").text}')
# С помощью поиска по занчению атрибута ID=R01235 и вложенного элемента Value выводим содержимое этого элемена т.е курс доллара США
print(root.find("*[@ID='R01235']/Value").text)
