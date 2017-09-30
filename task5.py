# Multistep Adams method
from prettytable import PrettyTable
from math import tan
from numpy import linspace

def f(x,y):
    return (y+x)**2

y = [0]
x = [0,0.1,0.2,0.3]
# y_1, y_2 and y_3 were found using Runge-Kutta method
y += [0.000334589,0.002709878,0.009336039]
delta = []
y_ex = []

h = 0.1
for i in range(4,11):
    x += [h*i]
    y += [round(y[i-1]+h/24*(55*f(x[i-1],y[i-1])-59*f(x[i-2],y[i-2])+37*f(x[i-3],y[i-3])-9*f(x[i-4],y[i-4])),9)]
    delta += [h*f(x[i],y[i])]
print(y)

for i in range(11):
    y_ex += [round(tan(h*i)-h*i,9)]

print(y_ex)	
	
table = PrettyTable()
table.add_column('k',[i for i in range(11)])
table.add_column('x',[x for x in linspace(0.0, 1.0, num=11, endpoint=True)])
table.add_column('y',y[0:11])
table.add_column('f(x_k,y_k)',[f(x[i],y[i]) for i in range(11)])
table.add_column('y_ист',y_ex)
table.add_column('e',[abs(y[i]-y_ex[i]) for i in range(11)])
print(table)	