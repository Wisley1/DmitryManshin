# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import seaborn as sns
import itertools
import math
pd.set_option('display.max_columns', None)

# Press the green button in the gutter to run the script.
print('Введите количество исследуемых факторов:')
k = int(input())

num_exp = 2**k
print('Число всех экспериментов будет равно:', num_exp)
matrix_plan = pd.DataFrame({'№ эскперимента': [i for i in range(1,num_exp+1)]}) #создание строк с номером эксперимента

#for j in range(1,k+1):
matrix_plan['Z1'] = ['1','1', '1', '1', '1', '1', '1', '1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1']
matrix_plan['Z2'] = ['1','1', '1', '1', '-1', '-1', '-1', '-1', '1', '1', '1', '1', '-1', '-1', '-1', '-1']
matrix_plan['Z3'] = ['1','1', '-1', '-1', '1', '1', '-1', '-1', '1', '1', '-1', '-1', '1', '1', '-1', '-1']
matrix_plan['Z4'] = ['1','-1', '1', '-1', '1', '-1', '1', '-1', '1', '-1', '1', '-1', '1', '-1', '1', '-1']

print('Введите результаты опытов для первого фактора через запятую')
first_factor = input().split(',')
matrix_plan['y1'] = [first_factor[i] for i in range(num_exp)]
matrix_plan['y2'] = [first_factor[i] for i in range(num_exp)]
matrix_plan['y3'] = [first_factor[i] for i in range(num_exp)]
matrix_plan['y4'] = [first_factor[i] for i in range(num_exp)]
print(matrix_plan) #table 1

#for j in range(1,k+1)
print('Введите верхние уровни указанных ранее факторов через запятую')
levels_up = input().split(',')
print('Введите нижние уровни указанных ранее факторов через запятую')
levels_down = input().split(',')


middle = []
interval_var = []
correlation = []


for i in range(k):
    middle.append((float(levels_up[i])+float(levels_down[i]))/2)
    interval_var.append(float(levels_up[i])-float(levels_down[i])/2)
    correlation.append(f'(Z{i} - {middle[i]})/{interval_var[i]}')
cod_factors = pd.DataFrame({'Факторы': ['Z1','Z2','Z3','Z4'], 'Верхний уровень Zi': [float(levels_up[i]) for i in range(k)],
                            'Нижний уровень Zi': [float(levels_down[i]) for i in range(k)],
                            'Центр Z': [middle[i] for i in range(k)],
                            'Интервал варьирования': [interval_var[i] for i in range(k)]})
print(cod_factors) #table 2



matrix_plan['y_mean'] = matrix_plan[['y1','y2','y3','y4']].mean(axis=1)

print(matrix_plan)