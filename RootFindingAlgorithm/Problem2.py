import matplotlib.pyplot as plt

def func(x):
    return ((4+x)/(((42-2*x)**2)*(28-x)))-.016

def graph_plot():
    y = []
    x = 0;
    x_list=[]
    while x <= 20:
        y.append(func(x))
        x_list.append(x)
        x=x+1
    plt.plot(x_list,y)
    plt.ylabel("Function value")
    plt.xlabel("x value")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

graph_plot()
