"""
Created on Mon May  3 16:18:28 2021

@author: Ana Caroline
"""
import numpy as np
import matplotlib.pyplot as grafico

def f(x):
    y =  x**5 + 3*x + 5
    return y

def f_dif(theta, x, m):
    y = np.cos(m*theta - x*np.sin(theta))
    return y

def simpson(a, b, f, N):
    dx = (b - a)/N
    soma_imp = 0
    soma_par = 0
    for i in range(1,N,2):
        soma_imp +=f(a+i*dx)
        
    for i in range(2, N, 2):
        soma_par += f(a+i*dx)
    
    return (dx/3)*(f(a) + f(b) + 4*soma_imp + 2*soma_par)

def Bessel(m, x, f_dif, N_theta):
    dtheta = np.pi/N_theta
    soma_imp = 0
    soma_par = 0
    for i in range(1,N_theta,2):
        soma_imp +=f_dif(i*dtheta, x, m)
        
    for i in range(2, N_theta, 2):
        soma_par += f_dif(i*dtheta, x, m)
    
    return ((dtheta/3)*(f_dif(0, x, m) + f_dif(np.pi, x, m) + 4*soma_imp + 2*soma_par))/np.pi

'''Programa Principal'''
##Simpson da função polinomial
a = 0
b = 1
N = 10

##Simpson de Bessel
x = np.linspace(0,20, 100)
N_theta = 100
grafico.plot(x, Bessel(0, x, f_dif, N_theta), label = "m = 0")
grafico.plot(x, Bessel(1, x, f_dif, N_theta), label = "m = 1")
grafico.plot(x, Bessel(2, x, f_dif, N_theta), label = "m = 2")
grafico.legend()
grafico.show()

