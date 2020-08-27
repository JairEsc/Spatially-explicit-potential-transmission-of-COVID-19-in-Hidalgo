# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:04:36 2020

@author: jair
"""

import numpy as np
import matplotlib.pyplot as plt

dias=[];
ajuste=[];
ajuste_casos_diarios=[]
ajuste_acumulados=[];


datos_reales_diarios=[2,
         1,
         0,
         0,
         5,
         2,
         0,
         0,
         2,
         0,
         5,
         0,
         2,
         2,
         5,
         4,
         2,
         2,
         1,
         6,
         5,
         1,
         4,
         2,
         5,
         0,
         6,
         0,
         3,
         3,
         5,
         12,
         5,
         14,
         19,
         3,
         27,
         10,
         17,
         8,
         36,
         16,
         19,
         21,
         24,
         6,
         22,
         40,
         22,
         35,
         44,
         21,
         44,
         34,
         29,
         34,
         43,
         68,
         64,
         32,
         76,
         46,
         68,
         63,
         39,
         56,
         51,
         76,
         120,
         40,
         65,
         55,
         71,
         40,
         59,
         129,
         113,
         66,
         54,
         65,
         74,
         21,
         54,
         115,
         58,
         98,
         59,
         64,
         51,
         70,
         123,
         57,
         87,
         56,
         65,
         52,
         120,
         62,
         97,
         68,
         77,
         38,
         20,
         84,
         111,
         102,
         90,
         55,
         98,
         27,
         97,
         69,
         68,
         93,
         55,
         81,
         52,
         96,
         75,
         99,
         58,
         151,
         109,
         38,
         109,
         74,
         225,
         80,
         136,
         123,
         71,
         159,
         77,
         144,
         61,
         152,
         93,
         124,
         67,
         86,
         171,
         176,
         155,
         61,
         111,
         158,
         45,
         159,
         110,
         186,
         126,
         96,
         126]


reales_acumulados=[]
t=[]
ac=0;
for i in range (0, 145):
    dias.append(i);
    ac=ac+datos_reales_diarios[i];
    reales_acumulados.append(ac)
for i in range (0, 400):
    t.append(i)
    #ajuste_casos_diarios.append(((-510.05953*np.exp(-np.exp(-0.05260*(i-38.02783))))*(-0.05260*np.exp(-0.05260*(i-38.02783)))))
    ajuste_casos_diarios.append(((-19370*np.exp(-np.exp(-.01426*(i-136.6))))*(-.01426*np.exp(-.01426*(i-136.6)))))

ac=0
for i in range(0,len(ajuste_casos_diarios)):
    ac=ac+ajuste_casos_diarios[i]
    ajuste_acumulados.append(ac)

plt.figure(figsize=(12,8))
#Graficar reales y teoricos (se debe ajustar el rango del ciclo a 153)
plt.plot(dias,reales_acumulados,t,ajuste_acumulados)

plt.legend(['Casos reales acumulados','Casos teóricos acumulados'])
