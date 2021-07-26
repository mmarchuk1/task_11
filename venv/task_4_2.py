'''
Дан список целых чисел. Подсчитать сколько четных чисел в списке
'''
x = 5
a = list(range(x))
n = 0
for i in range(x):
    if a[i] % 2 == 0:
        n += 1
print(a)
print(n)