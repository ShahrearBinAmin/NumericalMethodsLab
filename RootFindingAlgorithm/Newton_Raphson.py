import matplotlib.pyplot as plt



def func(x):
    return x**3-.165*x**2+3.993*10**(-4)

def derivative(x):
    return 3*x**2-.33*x


def graph_plot():
    y = []
    x = -3;
    x_list=[]
    while x <= 10:
        y.append(func(x))
        x_list.append(x)
        x=x+.1

    plt.plot(x_list,y)
    plt.ylabel("Function value")
    plt.xlabel("x value")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    return

x0=.05
print("")
while True:
    x1=x0-(func(x0)/derivative(x0))
    print(x1)
    if abs((x0-x1)/x1)<.0001:
        break
    x0=x1

graph_plot()