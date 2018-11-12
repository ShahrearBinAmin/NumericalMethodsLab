from math import exp
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    #return x**3-.165*x**2+3.993*10**-4
    return np.exp(x)-5*x**2

def plot():
    x_value=[]
    y_value=[]
    i=-1
    while i<=1:
        x_value.append(i)
        y_value.append(func(i))
        i = i + .1
    plt.plot(x_value,y_value)
    plt.ion()
    plt.show()
    #plt.interactive(False)
    print(x_value)
    print(y_value)
    return 1

def smart_plot():
    x=np.arange(-1.0,1.0,.1)
    plt.plot(x,func(x),'bo',x,func(x),'k')
    plt.ylabel("Function value")
    plt.xlabel("x value")
    plt.grid(True)
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.show()
    return 1

# with error of EPSILON
def bisection(a, b):
    c = a
    step=0
    reletive_error=[]
    while (abs(b - a) > 0.00001):
        reletive_error.append(abs(b-a))
        step=step+1
        c = (a + b) / 2
        if (func(c) == 0.0):
            break
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)
    plt.plot(range(step),reletive_error,'ro',range(step),reletive_error,'k')
    plt.ylabel("Error")
    plt.xlabel("Iteration")
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

def main():
    a = 1
    b = 0
    # print(str(func(a)) + "  " + str(func(b)))
    bisection(a, b)
    #plot()
    smart_plot()

if __name__ == "__main__":
	main()
