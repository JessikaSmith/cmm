from prettytable import PrettyTable
from math import tan
from numpy import linspace

print('task4 "Runge-Kutta method"')
x_max = 0.5
x_min = 0
w_0 = 0
h = 0.1
num_step = round((x_max-x_min)/h,1)

w = []
y_ex = []

for i in range(6):
	if i == 0:
		w = [w_0]
		y_ex += [round(tan(w_0)-w_0,9)]
	else:
		w_i = w[i-1]
		t_i = round((i-1)*0.1,1)
		k_1 = h*(t_i+w_i)**2
		k_2 = h*(t_i+h/2+w_i+k_1/2)**2
		k_3 = h*(t_i+h/2+w_i+k_2/2)**2
		k_4 = h*(t_i+h+w_i+k_3)**2
		w += [round(w_i+1/6*(k_1+2*k_2+2*k_3+k_4),9)]
		y_ex += [round(tan(t_i)-t_i,9)]
y_ex += [round(tan(0.5)-0.5,9)]
y_ex = y_ex[1:]
eps = [abs(w[i]-y_ex[i]) for i in range(6)]
eps = [round(eps[i],9) for i in range(6)]

table = PrettyTable()
table.add_column('k',[i for i in range(6)])
table.add_column('x',[x for x in linspace(0.0, 0.5, num=6, endpoint=True)])
table.add_column('w',w)
table.add_column('y_r',y_ex)
table.add_column('eps',eps)
print(table)	