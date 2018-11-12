import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd


def func(x):
    return (x-1)**3+.512

def derivative(x):
    return 3*(x-1)**2

def func3(x):
    return x**2+2

def derivative3(x):
    return 2*x

def func4(x):
    return x**3-.165*x**2+3.993*10**(-4)

def derivative4(x):
    return 3*x**2-.33*x

def graph_plot():
    y = []
    x = -10;
    x_list=[]
    while x <= 10:
        y.append(func3(x))
        x_list.append(x)
        x=x+.1

    plt.plot(x_list,y)
    plt.ylabel("Function value")
    plt.xlabel("x value")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    return

all_input=input()
x0=float(all_input.split(' ')[0])
iteration=int(all_input.split(' ')[1])
itr_count=0
DECIMAL=20
# print("Iteration\t\txi\t\tf(xi)\t\t\tf`(x)\t\t\tError %")
x0_list=[round(x0,DECIMAL)]
fnc_x0=[round(func4(x0),DECIMAL)]
drv_x0=[round(derivative4(x0),DECIMAL)]
error_list=['XX']



while True:
    x1 = x0-(func4(x0)/derivative4(x0))
    itr_count=itr_count+1
    rel_error=abs((x0-x1)/x1)

    x0_list.append(round(x1,DECIMAL))
    fnc_x0.append(round(func4(x1),DECIMAL))
    drv_x0.append(round(derivative4(x1),DECIMAL))
    error_list.append(round(rel_error*100,DECIMAL))
    if rel_error<.00001:
        break
    if itr_count==iteration:
        print("Max number of iteration completed")
        break
    x0=x1

#graph_plot()
Dataset=list(zip(x0_list,fnc_x0,drv_x0,error_list))
df = pd.DataFrame(data = Dataset, columns=['xi', 'f(xi)','f`(xi)','Error %'])
print(df)
