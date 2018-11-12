#!/usr/bin/env python3
import numpy as np
def func(x):
    return 8*np.sin(x)*np.exp(-x)-1

def secant(x0,x00,a,iteration):
    print("{}\t\t{}\t\t\t{}\t\t{}\t\t\t{}\t\t{}"
          "".format("Itr", "Upper", "Lower", "Xm", "f(Xm)","Relative error"))
    print("-" * 75)
    itr_count=0
    while True:
        x1 = x0 - (func(x0) * (x0 - x00)) / (func(x0) - func(x00))
        itr_count = itr_count + 1
        rel_error = abs((x0 - x1) / x1)
        if(itr_count==1):
            print("{:2d} {:12f} {:12f} {:12f} {:15f}".format(itr_count, round(x0, 5),
            round(x00, 5), round(x1, 15), round(func(x1), 15)))
        else:
            print("{:2d} {:12f} {:12f} {:12f} {:15f} {:15f}".format(itr_count, round(x0, 5),
             round(x00, 5), round(x1, 15), round(func(x1), 15),round(rel_error * 100, 5)))

        if rel_error < a:
            break
        if itr_count == iteration:
            print("Max number of iteration completed")
            break
        x00 = x0
        x0 = x1
    print("Root is : ",x1)

print("8sin(x)e^(-x)-1")
all_input = input("Give Xi,Xi-1 ,Accuracy\n")
Xo = float(all_input.split(' ')[0])
Xoo = float(all_input.split(' ')[1])
accuracy=float(all_input.split(' ')[2])

secant(Xo,Xoo,accuracy,200)