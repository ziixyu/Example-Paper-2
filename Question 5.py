import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 50)
f = np.sin(x) + 0.2*np.cos(10*x)

def ThreePointAvg(f):
    g = np.zeros(len(f))
    for loop in range(1, len(f) - 1):
        g[loop] = (f[loop-1] + f[loop] + f[loop+1])/3
    g[0] = f[0]
    g[-1] = f[-1]
    return g

y = ThreePointAvg(f)
plt.plot(x,f)
plt.plot(x,y)
plt.show()