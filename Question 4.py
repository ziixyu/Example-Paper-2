import numpy as np
def f(x):
    return (x**2)*np.sin(x**2)

def twosided(x,h):
    return (f(x + h)- f(x- h))/(2*h)

def complexstep(x,h):
    return f(x + h*1j).imag/h

def dfdx(x): 
    """Evaluate derivative of x^2*sin(x^2)""" 
    return x*x*2*x*np.cos(x*x) + 2*x*np.sin(x*x)

for x in [10,100,1000,10000]:
    print("x:", x)
    for h in [10**-9,10**-12,10**-15]:
        print("h:", h)
        TwoValue = twosided(x,h)
        ComplexValue = complexstep(x,h)
        TrueValue = dfdx(x)
        print("Rel Error Two-Sided: {:.2e}".format(abs((TwoValue - TrueValue)/TrueValue)))
        print("Rel Error Complex-Step: {:.2e}".format(abs((ComplexValue - TrueValue)/TrueValue)))