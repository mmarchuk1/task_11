N = int(input('Введите количество гостей '))
if N  > 50:
  print('ресторан')
elif 20 <= N <= 50:
  print('кафе')
else:
  print('дома')