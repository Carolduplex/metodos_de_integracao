"""
Created on Mon Apr 26 16:25:37 2021

@author: Ana Caroline
"""
import numpy as np
import matplotlib.pyplot as grafico

pontos=np.array([[-8.8, 12.6],[-2.3,6.2],[2.7,8.4],[1.4,-14.9],[5.1,18.8]])

def neville(x, pontos):
    n=pontos.shape[0]
    matriz = np.zeros((n,n))
    '''for k in range(n):
        matriz[k,0] = pontos[k,1]
    '''
    matriz[:,0]=pontos[:,1]    
    for j in range(1,n,1):
        for i in range(0,n-j,1):
            matriz[i,j] = (1/(pontos[i,0] - pontos[(i+j),0]))*(((x - pontos[(i+j),0])*matriz[i,j-1]) - (x - pontos[i,0])*matriz[i+1,j-1])
    
    p = matriz[0,n-1]
    return p


x_range = np.linspace(-10,10,100)
y = []

for x in x_range:
  y.append(neville(x,pontos))
y=np.array(y)

grafico.plot(x_range,y, 'k', label= 'P(x)')  # plotando o polinômio interpolador
grafico.scatter(pontos[:,0],pontos[:,1], label='dados') #plotando os pontos de entrada
grafico.xlabel('x')
grafico.ylabel('y')
grafico.legend()
grafico.show()
