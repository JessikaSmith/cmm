from prettytable import PrettyTable
from math import tan
from numpy import arange, linspace

def function(x,y):
	(y+x)**2

def euler(function,y_0,x_min,x_max,step):
	y = [y_0]
	my_iter = iter(y)
	for h in range(x_min,x_max+1,step):
		y_i = next(y)
		y+=[y_i + h*function(x,y_1)]
	return y
		
	
def exact(ex_function,x_min,x_max,step):
	
	for h in range(x_min,x_max+1,step):
		pass
		#y_exact = 
	

def delta_y():
	pass
	
def create_table():
	pass

def recur(x):
	print("factorial has been called with n = " + str(x))
	if x == 0:
		return 0
	else:
		result = (x+recur(round(x-0.1,1)))**2
		print(result)
	
arange(0,0.6,0.1)

y_0 = 0
x_min = 0
x_max = 0.5
step = 0.1
#y1 = euler(function,y_0,x_min,x_max,step)
#ex_function = tan(x)-x
res = []
print(recur(0.5))
	