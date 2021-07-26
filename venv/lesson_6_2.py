'''Есть список словарей со учениками и их оценками по 3 предметам. Пример:
{
‘name’: ‘John Smith’,
‘math’: 10,
‘phys’: 9,
‘chem’: 5,
}
Создать список словарей, содержащих имя и среднюю оценку каждого
ученика. Список отсортировать по значению средней оценки.'''


dict_1 =[{'name': 'John Smith', 'math': 10, 'phys': 9, 'chem': 5},
         {'name': 'Alex White', 'math': 9, 'phys': 8, 'chem': 7},
         {'name': 'Mike Black', 'math': 8, 'phys': 8, 'chem': 7}]
result = []
for value in dict_1:
    avg = (value['math']+value['phys']+value['chem'])/3
    dict_11 ={}
    dict_11['name'] = value['name']
    dict_11['avg'] = avg
    result.append(dict_11)

a = [list(b.items()) for b in result]
print(a)




