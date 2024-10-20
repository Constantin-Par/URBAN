#
# Создается файл с количественным параметром по датам.
# Сохраняется на диск.
# Затем в нем проиводится суммирование по фамилиям и файл сохраняется на диск под другим именем.
#
import pandas as pd
from datetime import datetime, timedelta
names = ['Иванов', 'Петров', 'Сидоров']
sd = datetime.now()
data = {'Дата': [], 'Количество': [], 'Фамилия': []}
for i in range(5):
    date = sd + timedelta(days=i)
    for name in names:
        data['Дата'].append(date.strftime('%Y-%m-%d'))
        data['Количество'].append(i + 1)
        data['Фамилия'].append(name)
df = pd.DataFrame(data)
file = 'report.xlsx'
df.to_excel(file, index=False)
summary = df.groupby('Фамилия', as_index=False)['Количество'].sum()
file = 'report_sum.xlsx'
summary.to_excel(file, index=False)
print(f"Данные записаны в файл '{file}'")
