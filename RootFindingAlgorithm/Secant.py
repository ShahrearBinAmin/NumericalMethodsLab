import matplotlib.pyplot as plt

def func(x):
    return x**3-.165*x**2+3.993*10**(-4)

def graph_plot():
    y = []
    x = -10;
    x_list=[]
    while x <= 10:
        y.append(func(x))
        x_list.append(x)
        x=x+.1

    plt.plot(x_list,y)
    plt.ylabel("y(x)")
    plt.xlabel("x value")
    plt.title("Graph Plot")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    return

all_input=input()
x00=float(all_input.split(' ')[0])
x0=float(all_input.split(' ')[1])
# iteration=int(all_input.split(' ')[1])
iteration=30
itr_count=0

DECIMAL=4

print("Iteration\t\tX(i-1)\t\tXi\t\tX(i+1)\t\t\t\tf(xi)\t\t\t\t\t\tError %")
while True:
    x1 = x0-(func(x0)*(x0-x00))/(func(x0)-func(x00))
    itr_count=itr_count+1
    rel_error=abs((x0-x1)/x1)
    if itr_count==0:
        print("0\t\t\t\t", round(x00,DECIMAL), "\t\t", round(x0,DECIMAL),"\t\t",round(x1,DECIMAL),"\t\t",func(x1),"\t\tXX")
    else:
        print(itr_count,"\t\t\t\t", round(x00,DECIMAL), "\t\t", round(x0,DECIMAL), "\t\t", round(x1,DECIMAL), "\t\t", func(x1), "\t\t",round(rel_error*100,DECIMAL))
    if rel_error<.00001:
        break
    if itr_count == iteration:
        print("Max number of iteration completed")
        break
    x00 = x0
    x0 = x1

graph_plot()