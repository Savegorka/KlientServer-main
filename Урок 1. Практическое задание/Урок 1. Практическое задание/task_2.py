"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
a = [b'class', b'function', b'method']
for i in a:
    print(type(i))
    print(i)
    print(len(i))
    print('---')

"""
<class 'bytes'>
b'class'
5
---
<class 'bytes'>
b'function'
8
---
<class 'bytes'>
b'method'
6
---
"""