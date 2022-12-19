workday = 5
day_list = [1,2,3,4,5,6,7]
for i in range(7):
    day = int(input(('Введите число от 1 до 7',i,': ')))
    if day > workday:
        print('Да')
    else:
        print('Нет')