"""
 В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то
же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть
не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из
трех классов.
"""

a = 28
aTables = a / 2
aTablesInt = a // 2
b = 29
bTables = b / 2
bTablesInt = b // 2
c = 31
cTables = c / 2
cTablesInt = c // 2



if (aTables == aTablesInt):
    print(aTablesInt)
else:
    print(aTablesInt + 1)


if (bTables == bTablesInt):
    print(bTablesInt)
else:
    print(bTablesInt + 1)


if (cTables == cTablesInt):
    print(cTablesInt)
else:
    print(cTablesInt + 1)