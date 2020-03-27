import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N=100000

IN0 = 0
IQ0 = 1
R0 = 0
E0= 0
I0 = IN0 + IQ0
S0 = N - I0 - R0 - E0
S0 = S0
D0 = 0

#constants
gamma = 0.04 
beta = 0.8 / N #Transmission Coefficient
prob = .4 #prob of quarrantined
rs = 3  #rate of development of symptoms
k = 0    #infectiousness of exposed/asymptomatic cases, relative to symptomatic cases
u = 0.02  #per capita  death rate



BRP = 1.5
BRN = 4

t = np.linspace(0,300,300)

def deriv(y,t,N,beta,rs,prob,k,gamma,u):
    S,E,IQ,IN,R,D = y
  
    lamda = (beta * (IN)) #+ k * beta * E) 
    
    dSdt = -lamda * S
    dEdt = lamda * S - rs * E
    #print(E)
    dIQdt = rs * prob * E - gamma * IQ - u * IQ
    #print(IQ)
    dINdt = rs * (1-prob) * E - gamma * IN - u * IN
    dRdt = gamma * IQ + gamma * IN
    dDdt = u * (IQ + IN)

    return dSdt, dEdt , dIQdt , dINdt, dRdt , dDdt


y0 = S0,E0,IQ0,IN0,R0,D0


ret = odeint(deriv, y0,t,args=(N,beta,rs, prob,k,gamma,u))



S,E,IQ,IN,R,D = ret.T



fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, E, 'c', alpha=0.5, lw=2, label='Exposed')
ax.plot(t, IQ, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, IN, 'y', alpha=0.5, lw=2, label='Infected & Not Quarrantined')
ax.plot(t,  R, 'g', alpha=0.5, lw=2, label='Recovered')
ax.plot(t, D, 'black', alpha=0.5, lw=2, label='dead')

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
plt.savefig("temp.png")


def result():
    return (ret.T).tolist()