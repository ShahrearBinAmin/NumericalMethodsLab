#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import csv

def func(m):
    immidiate = (9.8*m)/15
    imi2=-(15/m)*9
    return immidiate*(1-np.exp(imi2))-35

def funciton_value(x_start,x_end):
    print("\t\tx\t\t\tf(x)\n","-"*25)
    while x_start<x_end:
        print("{:12f}{:12f}".format(x_start,func(x_start)))
        x_start=x_start+.1

def univariate(x_value, y_value, graph_info , x1_value=None,y1_value=None):
    if x1_value is not None:
        plt.plot(x_value, y_value,color='blue',label="bisection")
        plt.plot(x1_value,y1_value,color='red',label="false position")
    else:
        plt.plot(x_value, y_value,label=graph_info["method"])
    plt.xlabel(graph_info["x_label"])
    plt.ylabel(graph_info["y_label"])
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid()
    plt.title(graph_info["method"]+"\n"+graph_info["title"])
    plt.legend()
    plt.savefig(graph_info["method"]+" "+graph_info["title"]+".png", dpi=100)
    plt.show()

def bisection(a,lo,hi):
    print("Bisection: ")
    xm=0
    Xm=[]
    Iteration=[]
    error=[]
    if(func(lo)*func(hi)>0):
        print("Value does not exists ")
        return
    else:
        print("Root exists")
    iter_count=0
    print("{}\t{}\t  {}\t\t{}\t\t\t{}\t\t{}"
          "".format("Itr","Upper value","Lower value","Xm","f(Xm)","Relative error"))
    print("-" * 60)
    with open("data.csv", 'w') as csvfile:
        data = csv.writer(csvfile, delimiter=',')
        while (abs(lo - hi) > a):
            iter_count = iter_count + 1
            xo = xm
            xm = (lo + hi) / 2
            y = func(xm)
            rel_error = round((abs((xm - xo) / xm) * 100), 5);
            Xm.append(round(xm, 5))
            Iteration.append(iter_count)
            error.append(rel_error)
            data.writerow([xm, rel_error])
            print("{:2d} {:12f} {:12f} {:12f} {:15.3e} {:15f}".format(iter_count, round(hi, 5),
                                                                      round(lo, 5), round(xm, 5), round(y, 15),
                                                                      round((abs((xm - xo) / xm) * 100), 5)))
            if (y * func(hi) > 0):
                hi = xm
            else:
                lo = xm
        print("\nRoot is : ", xm,"\n")
        return Xm, Iteration, error

def false_position(a,lo,hi):
    print("False position: ")
    Xm = []
    Iteration = []
    error = []
    xm = 0
    if(func(lo)*func(hi)>0):
        print("Value does not exists ")
        return
    iter_count=0
    print("{}\t{}\t  {}\t\t{}\t\t\t{}\t\t{}"
          "".format("Itr", "Upper value", "Lower value", "Xm", "f(Xm)", "Relative error"))
    print("-" * 60)
    while(True):
        iter_count=iter_count+1
        xp=xm
        fx1=func(hi)
        fx0=func(lo)
        xm=-((fx0*(lo-hi))/(fx0-fx1))+lo
        y=func(xm)
        rel_error = round((abs((xm-xp)/xm)*100),5)
        Xm.append(round(xm, 5))
        Iteration.append(iter_count)
        error.append(rel_error)
        print("{:2d} {:12f} {:12f} {:12f} {:15.3e} {:15f}".format(iter_count,round(hi,5),
                    round(lo,5),round(xm,5),round(y,15),round((abs((xm-xp)/xm)*100),5)))
        if(y>0):
            hi=xm
        else:
            lo=xm
        if(abs((xm-xp)/xm)<a):
            print("\nRoot is : ",xm)
            break
    return Xm, Iteration, error

funciton_value(55,70)
all_input = input("Give a, low ,high\n")
a = float(all_input.split(' ')[0])
lo = float(all_input.split(' ')[1])
hi = float(all_input.split(' ')[2])
xm,iter_b,error_b=bisection(a,lo,hi)
univariate(x_value=xm, y_value=error_b,graph_info={"x_label": "Xm", "y_label": "Relative error",
                          "title":"Xm Vs Relative error","method":"Bisection"})
univariate(x_value=iter_b,y_value=error_b,graph_info= {"x_label": "Iteration", "y_label": "Relative error",
                            "title":"Iteration Vs Relative error","method":"Bisection"})
xr,iter_f,error_f=false_position(a,lo,hi)
univariate(x_value=xr,y_value=error_f, graph_info={"x_label": "Xr", "y_label": "Relative error",
                          "title":"Xr Vs Relative error","method":"False Position"})
univariate(x_value=iter_f,y_value= error_f,graph_info={"x_label": "Iteration", "y_label": "Relative error",
                          "title":"Iteration Vs Relative error","method":"False Position"})
univariate(x_value=iter_b,y_value=error_b,graph_info={"x_label":"Iteration","y_label":"Relative error","title":
                          "Bisection & False Position","method":"Compare"},x1_value=iter_f,y1_value=error_f)
univariate(x_value=xm,y_value=error_b,graph_info={"x_label":"X","y_label":"Relative error","title":
                          "Bisection & False Position","method":"Compare2"},x1_value=xr,y1_value=error_f)
