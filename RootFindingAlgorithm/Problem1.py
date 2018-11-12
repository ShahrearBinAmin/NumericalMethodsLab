import matplotlib.pyplot as plt
import pandas as pd
import sys
def factorial(n):
    if(n>=1):
        return n*factorial(n-1)
    else:
        return 1

def func(x,n,k):
    temp= (x/2)**n
    totalsum=0
    for i in range(k):
        i=i+1
        sum=(((-1)**i)*((x**2)/4)**i)/(factorial(i)*factorial(n+i))
        totalsum=totalsum+sum
    return temp*totalsum

def func1(x):
    return x**3-.165*x**2+3.993*10**(-4)

def graph_plot():
    y = [[],[],[]]
    x = 0;
    x_list=[]
    while x <= 10:
        print(str(x)+"  "+str(func(x,0,10))+"\n")
        y[0].append(func(x,0,10))
        y[1].append(func(x,1,10))
        y[2].append(func(x,2,10))
        x_list.append(x)
        x=x+.1
    for i in range(3):
        plt.plot(x_list,y[i])
        plt.ylabel("Function value")
        plt.xlabel("x value")
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()
    return
def bisection():
    all_input = input("Give a, low ,high")
    a = float(all_input.split(' ')[0])
    lo = float(all_input.split(' ')[1])
    hi = float(all_input.split(' ')[2])
    # n = int(all_input.split(' ')[3])
    xm=0


    if(func1(lo)*func1(hi)>0):
        print("Value does not exists ")
        return
    iter_count=0
    while(abs(lo-hi)>a):
        iter_count=iter_count+1
        xo=xm
        xm=(lo+hi)/2
        y=func1(xm)
        print("{:2d} {:10f} {:10f} {:15.3e} {:15f}".format(iter_count,round(hi,5),
                    round(lo,5),round(y,15),round((abs((xm-xo)/xm)*100),2)))
        if(y*func1(hi)>0):
            hi=xm
        else:
            lo=xm

#graph_plot()
bisection()
