import datetime
import random
import numpy as np


# HOLIDAYS = '13, 15'

INPUT = 'input.txt'
OUTPUT = 'output.txt'

# отрываем файл для чтения
with open(INPUT, 'r', encoding='utf-8') as file:
    line_list = file.read().strip().split('\n')
    START_DATE = line_list[0]
    END_DATE = line_list[1]
    # список сотрудников
    employees = line_list[2:]

# перетусуем список
random.shuffle(employees)


def str_to_date(date: str):
    d, m, y = map(int, date.split("."))
    return datetime.date(y, m, d)

def get_holidays(days: str):
    # start_date: datetime.date, end_date: datetime.date
    days_list = days.split(',')
    return print(days_list)

start_date = str_to_date(START_DATE)
end_date = str_to_date(END_DATE)
delta = datetime.timedelta(days=1)

# список праздничных дней
# holidays_list = get_holidays(HOLIDAYS)

# генерим список рабочих дней
date_list = []
while(start_date <= end_date):
    if start_date.weekday() != 5 and start_date.weekday() != 6 :  # and not in HOLIDAYS
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
