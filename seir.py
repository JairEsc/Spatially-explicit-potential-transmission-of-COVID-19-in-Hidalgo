# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:59:47 2020

@author: jair
"""


import numpy as np
import matplotlib.pyplot as plt
def base_sir_model(init_vals, params, t):
    S_0, I_0, R_0 = init_vals
    S, I, R = [S_0], [I_0], [R_0]
    beta, gamma = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (beta*S[-1]*I[-1])*dt
        next_I = I[-1] + (beta*S[-1]*I[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        I.append(next_I)
        R.append(next_R)
    #return np.stack([S, E, I, R]).T
    return I

def base_seir_model_e(init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    #return np.stack([S, E, I, R]).T
    return I
def base_seir_model_i(init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    #return np.stack([S, E, I, R]).T
    return I
def base_seir_model_r(init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    #return np.stack([S, E, I, R]).T
    return R

def para_comparar(modelo):
    por_dias=[]
    for i in range(0,t_max+1):
        por_dias=np.append(por_dias,modelo[i*10])
    return por_dias
def suma_modelos(modelo1,modelo2):
    for i in range(0,len(modelo1)):
        modelo1[i]=modelo1[i]+modelo2[i]
    return (modelo1)
def tiempo_max(modelo):
    for i in range(0, len(modelo)):
        if (modelo[i]==np.max(modelo)):
            break
    return i
def parametro_min(modelo):
    for i in range(0, len(modelo)):
        if (modelo[i]==np.min(modelo)):
            break
    return i
def para_comparar(modelo):
    por_dias=[]
    for i in range(0,t_max+1):
        por_dias=np.append(por_dias,modelo[i*10])
    return por_dias
def negativo(modelo):
    for i in range(0,len(modelo)):
        modelo[i]=modelo[i]*-1
    return (modelo)
def error(modelo1,modelo2):
    error=0
    for i in range(0,min(len(modelo1),len(modelo2))):
        error=error+(modelo1[i]-modelo2[i])*(modelo1[i]-modelo2[i])
    return error
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

dias=np.linspace(0,len(datos_reales_diarios)-1,len(datos_reales_diarios))
t_max =50
dt = .1
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = 3065504
init_vals = N - 2,0, 2,0
alpha=0.19
gamma=0.344

plt.figure(figsize=(12,8))
plt.plot(t,base_seir_model_i([N-2-6,6,2,0],[.19,0.626/N,.344],t),dias,datos_reales_diarios)
plt.legend(['Infectados Teóricos','Muertos Acumulados Teóricos','Recuperados teóricos anterior, beta=0.66'])

