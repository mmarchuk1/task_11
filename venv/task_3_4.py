str1 = input('введите строку')
str_length = len(str1)
if str_length > 0:
    mid_symbol = str1[str_length // 2:str_length // 2 + 1:]
    print('Middle symbol:', mid_symbol)
    if str1[0] == mid_symbol:
        print(str1[1:str_length - 1:])
else:
    print('Empty string')