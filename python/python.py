import numpy as np
from scipy.integrate import odeint

# function that returns dy/dt
def model(y,t):
    k = 0.3
    dydt = -k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,10,1000)

# solve ODE
y = odeint(model,y0,t).flatten()
result = np.column_stack((t, y))
np.savetxt('data/python.csv', result, fmt="%f", delimiter=",")
