import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N=100000


R0 =0
I0 = 1
S0 = N - I0 - R0

#constants
gamma = 0.04
beta = 1.6 *.3  




BRP = 1.5
BRN = 4

t = np.linspace(0,100,100)

def deriv(y,t,N,beta,gamma):
    S,I,R = y
  
    lamda = beta * I / N
    
    dSdt = -lamda * S
    dIdt = lamda * S - gamma * I 
    dRdt = gamma * I 

    return dSdt, dIdt, dRdt


y0 = S0,I0,R0


ret = odeint(deriv, y0,t,args=(N,beta, gamma))

#print(ret)

S,I,R = ret.T

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R * .98, 'g', alpha=0.5, lw=2, label='Recoverd')
ax.plot(t, R * .04, 'black', alpha=0.5, lw=2, label='Dead')


ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,N)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
plt.savefig("temp3.png")
