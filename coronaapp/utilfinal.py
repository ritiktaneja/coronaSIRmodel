import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def deriv(y,t,N,beta,rs,prob,k,gamma,u):
    S,E,I,R,D = y

    lamda = beta * I
   
    dSdt = -lamda * S
    dEdt = lamda * S - rs * E
    #print(E)

    dIdt = lamda * S - gamma * I- u * I
    dRdt = gamma * I
    dDdt = u * (I)

    return dSdt, dEdt , dIdt, dRdt , dDdt


  


def result(N,R0,E0,I0,S0,D0,gamma,beta,rs,u):

    N=N
    R0 = R0
    E0= E0
    I0 = I0
     
    t = np.linspace(0,300,300)
    S0 = S0
    D0 = 0
    y0 = S0,E0,I0,R0,D0
    #constants
    gamma = gamma #0.04 
    beta = beta # 0.8 / N #Transmission Coefficient
  
    rs = rs #3  #rate of development of symptoms
    #infectiousness of exposed/asymptomatic cases, relative to symptomatic cases
    u = u #0.02  #per capita  death rate
    print(N,"$$")
    ret = odeint(deriv, y0,t,args=(N,beta,rs, 1,0,gamma,u))


    return (ret.T).tolist()






# S,E,I,R,D = odeint(deriv, y0,t,args=(N,beta,rs, prob,k,gamma,u)).T



# fig = plt.figure(facecolor='w')
# ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
# ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Susceptible')
# ax.plot(t, E, 'c', alpha=0.5, lw=2, label='Exposed')
# ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Infected')

# ax.plot(t,  R, 'g', alpha=0.5, lw=2, label='Recovered')
# ax.plot(t, D, 'black', alpha=0.5, lw=2, label='dead')

# ax.set_xlabel('Time /days')
# ax.set_ylabel('Number (1000s)')
# ax.set_ylim(0,N)
# ax.yaxis.set_tick_params(length=0)
# ax.xaxis.set_tick_params(length=0)
# ax.grid(b=True, which='major', c='w', lw=2, ls='-')
# legend = ax.legend()
# legend.get_frame().set_alpha(0.5)
# for spine in ('top', 'right', 'bottom', 'left'):
#     ax.spines[spine].set_visible(False)
# plt.show()
# plt.savefig("tempfinal.png")

