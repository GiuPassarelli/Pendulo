from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import *
from math import *

def EqDif(Y,t):
	teta = Y[0]
	w = Y[1]
	dtetadt = w
	dwdt = -g*(sin(teta))/l
	return [dtetadt, dwdt]

t = arange(0,3,0.001)
g = 9.8
l = 2
Y0=[radians(60),0]

sol = odeint(EqDif,Y0,t)

x = []
y = []

for i in sol[:,0]:
	y.append(sin(i)*l)
	x.append(cos(i)*l)

plt.plot(y, x)
plt.axis([min(y),max(y),max(x),min(x)])
plt.axis('equal')
plt.title('Posição do pêndulo')
plt.show()

plt.plot(t, x)
#plt.axis([min(t),max(t),max(x),min(x)])
plt.axis('equal')
plt.title('Posição X por tempo')
plt.show()

plt.plot(t, y)
#plt.axis([min(t),max(t),max(y),min(y)])
plt.axis('equal')
plt.title('Posição Y por tempo')
plt.show()