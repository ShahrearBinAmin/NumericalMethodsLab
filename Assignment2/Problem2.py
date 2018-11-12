#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
def func1(x):
    return -x**2+1.8*x+2.5

def derivative1(x):
    return -2*x+1.8

def func2(x):
    return np.exp(-.5*x)*(4-x)-2

def derivative2(x):
    return np.exp(-.5*x)*(.5*x-3)

def graph_plot(x_start,x_end):
    y = []
    x_list = []
    x =x_start
    while x <= x_end:
        y.append(derivative2(x))
        x_list.append(x)
        x = x+.1
    plt.plot(x_list,y)
    plt.ylabel("Derivative value")
    plt.xlabel("x value")
    plt.title("X vs Derivative")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.savefig("analysis"+".png", dpi=100)
    plt.show()
    return

def newton_raphson(func,derivative,x0,a,iteration):
    itr_count=0
    print(x0)
    print("{}\t\t\t{}\t\t{}\t\t{}\t\t\t{}"
          "".format("Itr", "Xi", "f(Xi)", "f'(Xi)", "Relative error"))
    print("-"*30,"Xo =",x0,"-"*30)
    while True:
        x1 = x0 - (func(x0) / derivative(x0))
        itr_count = itr_count + 1
        rel_error = abs((x0 - x1) / x1)
        if(itr_count==1):
            print("{:2d} {:12f} {:12f} {:12f}".format(itr_count, round(x1, 5),
            round(func(x1), 5), round(derivative(x1), 15)))
        else:
            print("{:2d} {:12f} {:12f} {:12f} {:15f}".format(itr_count, round(x1, 5),
            round(func(x1), 5), round(derivative(x1), 15),round(rel_error*100, 5)))
        if rel_error < a:
            print("\nRoot is : ",x1,"\n")
            break
        if itr_count == iteration:
            print("Max number of iteration completed")
            break
        x0 = x1

print("-x^2+1.8x+2.5")
all_input = input("Give Xo, Accuracy\n")
Xo = float(all_input.split(' ')[0])
a = float(all_input.split(' ')[1])
newton_raphson(func1,derivative1,Xo,a,100)
print("-"*60)
print("e^(-.5x)(4-x)-2")
graph_plot(-3,20)
newton_raphson(func2,derivative2,2,a,100)
newton_raphson(func2,derivative2,6,a,100)
newton_raphson(func2,derivative2,8,a,100)
