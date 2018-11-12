import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

def func(m):
    immidiate = (9.8*m)/15
    imi2=-(15/m)*9
    return immidiate*(1-np.exp(imi2))-35

def compare_graph(x_value,y_value,graph_info):
    plt.plot(x_value,y_value)
    plt.xlabel(graph_info["x_label"])
    plt.ylabel(graph_info["y_label"])
    plt.title(graph_info["title"])
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.savefig(graph_info["method"]+" "+graph_info["title"]+".png", dpi=100)
    plt.show()

def graph_plot():
    y = []
    x_list = []
    x =-100
    while x <= 300:
        y.append(func(x))
        x_list.append(x)
        x = x+5
    plt.plot(x_list,y)
    plt.ylabel("Function value")
    plt.xlabel("x value")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    Dataset = list(zip(x_list, y))
    df = pd.DataFrame(data=Dataset, columns=['xi', 'f(xi)'])
    print(df)
    return

def bisection(a,lo,hi):
    print("Bisection: ")
    xm=0
    Xm=[]
    Iteration=[]
    error=[]
    if(func(lo)*func(hi)>0):
        print("Value does not exists ")
        return
    iter_count=0
    print("{}\t{}\t  {}\t\t{}\t\t\t{}\t\t{}\n------------------------------------------------------------------------"
          "".format("Itr","Upper value","Lower value","Xm","f(Xm)","Relative error"))
    while(abs(lo-hi)>a):
        iter_count=iter_count+1
        xo=xm
        xm=(lo+hi)/2
        y=func(xm)
        rel_error=round((abs((xm-xo)/xm)*100),5);
        Xm.append(round(xm,5))
        Iteration.append(iter_count)
        error.append(rel_error)
        with open("data.csv",'w') as csvfile:
            data =csv.writer(csvfile,delimiter=',')
            data.writerow([xm,rel_error])
        print("{:2d} {:12f} {:12f} {:12f} {:15.3e} {:15f}".format(iter_count,round(hi,5),
                    round(lo,5),round(xm,5),round(y,15),round((abs((xm-xo)/xm)*100),5)))
        if(y*func(hi)>0):
            hi=xm
        else:
            lo=xm
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
    print("{}\t{}\t  {}\t\t{}\t\t\t{}\t\t{}\n------------------------------------------------------------------------"
          "".format("Itr", "Upper value", "Lower value", "Xm", "f(Xm)", "Relative error"))
    while(True):
        iter_count=iter_count+1
        xp=xm
        fx1=func(hi)
        fx0=func(lo)
        xm=-((fx0*(lo-hi))/(fx0-fx1))+lo
        y=func(xm)
        print("{:2d} {:12f} {:12f} {:12f} {:15.3e} {:15f}".format(iter_count,round(hi,5),
                    round(lo,5),round(xm,5),round(y,15),round((abs((xm-xp)/xm)*100),5)))
        if(y>0):
            lo=xm
        else:
            hi=xm
        if(abs((xm-xp)/xm)<a):
            break

#graph_plot()
all_input = input("Give a, low ,high")
a = float(all_input.split(' ')[0])
lo = float(all_input.split(' ')[1])
hi = float(all_input.split(' ')[2])
xm,iter,error=bisection(a,lo,hi)
compare_graph(xm,error,{"x_label": "Xm","y_label":"Relative error","title":"Xm Vs Relative error","method":"bisection"})
compare_graph(iter,error,{"x_label": "Iteration","y_label":"Relative error","title":"Iteration Vs Relative error","method":"bisection"})
false_position(a,lo,hi)
