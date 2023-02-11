import pandas as pd
from datetime import datetime

print('-'*50)
print('ДИАГНОСТИКА СЕЗОННЫХ ЗАБОЛЕВАНИЙ'.center(50))
print('-'*50)

print('Дата и время приёма: '.center(25), end='')
cur_datetime = datetime.now()
print(datetime.now().date(), '  ', cur_datetime.hour, ':', cur_datetime.minute)
print('Введите ФИО врача: '.center(25), end='')
fio_doctor = input()
print('Введите ФИО пациента: '.center(25), end='')
fio_patient = input()

# ищем клинические проявления в болезнях
print('*'*50)
print('Отметьте клинические проявления пациента из списка'.center(50))
print('*'*50)
clinical = pd.read_excel('table.xlsx', sheet_name=0)
clinical = pd.DataFrame(clinical)
print(str(clinical).center(100))
print('*введите id через пробел*'.center(50))
print('id: '.center(25), end='')
clinic = input().split()

print('-'*50)
print('Ваши клинические проявления: '.center(50))
for c in clinic:
    if int(c) - 1 < len(clinical) and int(c) - 1 >= 0:
        print(clinical.iloc[int(c)-1]['Клинические проявления'].center(50))
print('-'*50)

clinical_orvi = pd.read_excel('table.xlsx', sheet_name=1)
clinical_gripp = pd.read_excel('table.xlsx', sheet_name=2)
clinical_covid = pd.read_excel('table.xlsx', sheet_name=3)
clinical_orvi = pd.DataFrame(clinical_orvi)
clinical_gripp = pd.DataFrame(clinical_gripp)
clinical_covid = pd.DataFrame(clinical_covid)
k_orvi = 0
k_gripp = 0
k_covid = 0
for c in clinic:
    for i in range(len(clinical_orvi)):
        if clinical.iloc[int(c)-1]['Клинические проявления'] == clinical_orvi.iloc[i]['Клинические проявления ОРВИ']:
            k_orvi += 1
    for i in range(len(clinical_gripp)):
        if clinical.iloc[int(c)-1]['Клинические проявления'] == clinical_gripp.iloc[i]['Клинические проявления ГРИПП']:
            k_gripp += 1
    for i in range(len(clinical_covid)):
        if clinical.iloc[int(c)-1]['Клинические проявления'] == clinical_covid.iloc[i]['Клинические проявления КОВИД']:
            k_covid += 1

# ищем симптомы в болезнях
print('*'*50)
print('Отметьте симптомы пациента из списка'.center(50))
print('*'*50)
symptom = pd.read_excel('table.xlsx', sheet_name=4)
symptom = pd.DataFrame(symptom)
print(str(symptom).center(100))
print('*введите id через пробел*'.center(50))
print('id: '.center(25), end='')
symp = input().split()

print('-'*50)
print('Ваши симптомы: '.center(50))
for s in symp:
    if int(s) - 1 < len(symptom) and int(s) - 1 >= 0:
        print(symptom.iloc[int(s)-1]['Симптомы'].center(50))
print('-'*50)

symptom_orvi = pd.read_excel('table.xlsx', sheet_name=5)
symptom_gripp = pd.read_excel('table.xlsx', sheet_name=6)
symptom_covid = pd.read_excel('table.xlsx', sheet_name=7)
symptom_orvi = pd.DataFrame(symptom_orvi)
symptom_gripp = pd.DataFrame(symptom_gripp)
symptom_covid = pd.DataFrame(symptom_covid)
s_orvi = 0
s_gripp = 0
s_covid = 0
for s in symp:
    for i in range(len(symptom_orvi)):
        if symptom.iloc[int(s)-1]['Симптомы'] == symptom_orvi.iloc[i]['Симптомы ОРВИ']:
            s_orvi += 1
    for i in range(len(symptom_gripp)):
        if symptom.iloc[int(s)-1]['Симптомы'] == symptom_gripp.iloc[i]['Симптомы ГРИПП']:
            s_gripp += 1
    for i in range(len(symptom_covid)):
        if symptom.iloc[int(s)-1]['Симптомы'] == symptom_covid.iloc[i]['Симптомы КОВИД']:
            s_covid += 1



clinic_list = [k_orvi, k_gripp, k_covid]
symptom_list = [s_orvi, s_gripp, s_covid]

clinic_max = max(clinic_list)
symptom_max = max(symptom_list)

a = set()
b = set()

if clinic_max == k_orvi == k_gripp == k_covid:
    a = {'ОРВИ', 'ГРИПП', 'КОВИД'}
elif clinic_max == k_orvi == k_gripp:
    a = {'ОРВИ', 'ГРИПП'}
elif clinic_max == k_orvi == k_covid:
    a = {'ОРВИ', 'КОВИД'}
elif clinic_max == k_gripp == k_covid:
    a = {'ГРИПП', 'КОВИД'}
elif clinic_max == k_orvi:
    a = {'ОРВИ'}
elif clinic_max == k_gripp:
    a = {'ГРИПП'}
elif clinic_max == k_covid:
    a = {'КОВИД'}

if symptom_max == s_orvi == s_gripp == s_covid:
    b = {'ОРВИ', 'ГРИПП', 'КОВИД'}
elif symptom_max == s_orvi == s_gripp:
    b = {'ОРВИ', 'ГРИПП'}
elif symptom_max == s_orvi == s_covid:
    b = {'ОРВИ', 'КОВИД'}
elif symptom_max == s_gripp == s_covid:
    b = {'ГРИПП', 'КОВИД'}
elif symptom_max == s_orvi:
    b = {'ОРВИ'}
elif symptom_max == s_gripp:
    b = {'ГРИПП'}
elif symptom_max == s_covid:
    b = {'КОВИД'}

print('-'*50)
print('ИТОГОВЫЙ ДИАГНОЗ'.center(50), '\n')
if len(a & b) == 3 or len(a & b) == 2 or len(a & b) == 0:
    print('Невозможно точно определить диагноз'.center(50))
    print('Требуется пройти дополнительную диагностику!'.center(50))
    print('Обязательные лабораторные исследования'.center(50))
    print('ОРВИ'.center(50))
    print('- клинический анализ крови'.center(50))
    print('(нормоцитоз или лейкопения, ускорение СОЭ)'.center(50))
    print('- клинический анализ мочи'.center(50))
    print('(при неосложненном течении ОРВИ не должно быть изменений)'.center(50))
    print('ГРИПП'.center(50))
    print('- клинический анализ крови с определением'.center(50))
    print('лейкоцитарной формулы и времени кровотечения'.center(50))
    print('(характерна нормо-, либо лейкопения, при развитии'.center(50))
    print('бактериальных осложнений – лейкоцитоз)'.center(50))
    print('- клинический анализ мочи'.center(50))
    print('(при неосложненном гриппе возможна'.center(50))
    print('умеренная протеинурия, небольшая эритроцитурия)'.center(50))
    print('КОВИД'.center(50))
    print('- Проведения дифференциальной диагностики'.center(50))
    print(' на вирусы гриппа типа А и В, респираторно-синцитиальный вирус,'.center(50))
    print(' вирусы парагриппа, риновирусы, аденовирусы, человеческие'.center(50))
    print('метапневмовирусы, MERS-CoV'.center(50))
    print('- Обязательно проведение микробиологической диагностики'.center(50))
    print('и/или ПЦР-диагностики на Streptococcus pneumoniae,'.center(50))
    print('Haemophilus influenzae type B, Legionella pneumophila,'.center(50))
    print('а также иные возбудители бактериальных респираторных'.center(50))
    print('инфекций нижних дыхательных путей'.center(50))
elif len(a & b) == 1 and 'ОРВИ' in (a & b):
    print('ОРВИ'.center(50))
elif len(a & b) == 1 and 'ГРИПП' in (a & b):
    print('ГРИПП'.center(50))
elif len(a & b) == 1 and 'КОВИД' in (a & b):
    print('КОВИД'.center(50))
print('-'*50)
