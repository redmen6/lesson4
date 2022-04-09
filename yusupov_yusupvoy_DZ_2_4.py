some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for ind, element in enumerate(some_list):
    name = element.split(' ')[-1]
    print(f'Привет,{name.title()}!')
