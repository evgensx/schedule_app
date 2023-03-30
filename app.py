import datetime
import random
import numpy as np


INPUT = 'input.txt'
OUTPUT = 'output.txt'
HOLIDAYS = 'holidays.txt'

with open(HOLIDAYS, 'r', encoding='utf-8') as file:
    holidays_list = file.read().strip().split('\n')
    holidays = [datetime.datetime.strptime(x, "%d.%m.%Y") for x in holidays_list]


# отрываем файл для чтения
with open(INPUT, 'r', encoding='utf-8') as file:
    line_list = file.read().strip().split('\n')
    #дата начала и конца рассчета
    START_DATE = line_list[0]
    END_DATE = line_list[1]
    # список сотрудников
    employees = line_list[2:]

# перетасуем список
random.shuffle(employees)

start_date = datetime.datetime.strptime(START_DATE, "%d.%m.%Y")
end_date = datetime.datetime.strptime(END_DATE, "%d.%m.%Y")
delta = datetime.timedelta(days=1)

# генерим список рабочих дней
date_list = []
while(start_date <= end_date):
    if start_date.weekday() != 5 and start_date.weekday() != 6 and start_date not in holidays:
        date_list.append(start_date.strftime('%d.%m.%Y'))
    start_date += delta

# колечество рабочих дней в месяце
num_parts = len(date_list)

# создаем список работников
parts = np.array_split(employees, num_parts)

# записываем в выходный файл
with open(OUTPUT, 'w', encoding='utf-8') as file:
    file.write(f"{'Дата' : ^10} | {'Сотрудники' : <10}\n")
    for date, employees, num in zip(date_list, parts, range(num_parts)):
        file.write(f"{date} | {', '.join(str(x) for x in employees)}\n")
