import matplotlib.pyplot as plt



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
print("Iteration\t\txi\t\tf(xi)\t\t\tf`(x)\t\t\tError %")
print("0\t\t",round(x0,DECIMAL),"\t\t",round(func4(x0),DECIMAL),"\t\t",
       round(derivative4(x0),DECIMAL),"\t\tXX")


while True:
    x1 = x0-(func4(x0)/derivative4(x0))
    itr_count=itr_count+1
    rel_error=abs((x0-x1)/x1)
    print(str(itr_count)+"\t\t"+str(round(x1,DECIMAL))+"\t\t"+
          str(round(func4(x1),DECIMAL))+"\t\t"+str(round(derivative4(x1),DECIMAL))+
           "\t\t"+str(round(rel_error*100,DECIMAL)))
    if rel_error<.00001:
        break
    if itr_count==iteration:
        print("Max number of iteration completed")
        break
    x0=x1

#graph_plot()