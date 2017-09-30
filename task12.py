from math import tan
from prettytable import PrettyTable
import scipy as sc

y = [0]
y_ex = []
delta = []
xx = []

print('task1 "Euler method"')
for k in range(6):
	x = round(k*0.1,1)
	xx += [x]
	y += [round(y[k]+0.1*(y[k]+x)**2,9)]
	y_ex += [round(tan(x)-x,9)]
	delta += [round((0.1*(y[k]+x)**2),9)]

eps = [abs(y[i]-y_ex[i]) for i in range(6)]
eps = [round(eps[i],9) for i in range(6)]

k = [i for i in range(6)]

table = PrettyTable()
table.add_column('k',k)
table.add_column('x',xx)
table.add_column('y',y[:-1])
table.add_column('d(y)',delta)
table.add_column('y_r',y_ex)
table.add_column('eps',eps)
print(table)

print('task2 "Euler-Cauchy method"')
#Something is wrong with delta y
y_ex = []
delta = []
xx = []
y_w = []
y_i = [0]
for k in range(6):
	x = round(k*0.1,1)
	f = (y_i[k]+x)**2
	y_wave = y_i[k]+0.1*f
	y_w += [round(y_wave,9)]
	f_wave = (y_w[k]+x+0.1)**2
	y_i += [round(y_i[k] + 0.1*(f+f_wave)/2,9)]
	xx += [x]
	y_ex += [round(tan(x)-x,9)]
	delta += [round((0.1*(y_i[k]+x)**2),9)]

eps = [abs(y_i[i]-y_ex[i]) for i in range(6)]
eps = [round(eps[i],9) for i in range(6)]

print(y_w)
k = [i for i in range(6)]

table = PrettyTable()
table.add_column('k',k)
table.add_column('x',xx)
table.add_column('y',y_i[:-1])
table.add_column('y_wave',['']+y_w[:-1])
table.add_column('d(y)',delta)
table.add_column('y_r',y_ex)
table.add_column('eps',eps)
print(table)




