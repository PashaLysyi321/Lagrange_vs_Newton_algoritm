import math 
import random
import matplotlib.pyplot as plt

def first():
	yy = []
	xx = []
	yy2= []
	
	x  = 0.15
	forX = 0.3466 +0.4921*(x-0.3)/0.1 +0.0356*(x-0.3)*(x-0.2)/(2*0.1*0.1)-0.1116*(x-0.3)*(x-0.2)*(x-0.1)/(6*0.1*0.1*0.1) 
   
	print('For x = 0.15 answer is ')
	print(forX)
	print('----------------CHECK--------------') 
	print(math.cos(5*0.15-9))
	print('----------------Error--------------')
	print((math.fabs(forX - math.cos(5*0.15-9))))
	
	for i in range(0,1000):
		x  = random.random()
		xx.append(x) 
		pp =  0.3466 +0.4921*(x-0.3)/0.1 +0.0356*(x-0.3)*(x-0.2)/(2*0.1*0.1)-0.1116*(x-0.3)*(x-0.2)*(x-0.1)/(6*0.1*0.1*0.1)   
		yy.append(pp)
		mathcos = math.cos(5*x-9)
		yy2.append(mathcos)

	plt.scatter(xx,yy, c = 'blue', alpha = 1, label = 'Interpolation - Newton polynomial')
	plt.scatter(xx,yy2, c = 'red', alpha = 1, label = 'Math fuction')
	plt.title('Newton fuction vs math')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend(loc = 'lower right')
	plt.style.use('ggplot')
	plt.grid(True)
	plt.ylim([-1,1])
	plt.xlim([0,0.5])
	plt.show()
    
    
def second():
	x = [0,0.1,0.2,0.3]
	y = [0,0,0,0]
	for i in [0,1,2,3]:
		c = math.cos(5*x[i]-9)
		print('x' +' is ' +str(x[i])+ ' and y is '+str(c))
		y[i] = c
		
	print('------------------------------') 
	print('For x = 0.15 answer is ')
	numm = 0.15
	LL = y[0]*(numm-x[1])*(numm-x[2])*(numm-x[3])/((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3]))+y[1]*(numm-x[0])*(numm-x[2])*(numm-x[3])/((-x[0]+x[1])*(x[1]-x[2])*(x[1]-x[3]))+y[2]*(numm-x[0])*(numm-x[1])*(numm-x[3])/((-x[0]+x[2])*(-x[1]+x[2])*(x[2]-x[3]))+y[3]*(numm-x[0])*(numm-x[1])*(numm-x[2])/((-x[0]+x[3])*(-x[1]+x[3])*(x[3]-x[2]))
	print(LL)

	print('----------------CHECK--------------') 
	print(math.cos(5*numm-9))
	print('----------------Error--------------') 
	print(math.fabs(math.cos(5*numm-9) - LL))
	print('----------------plotly--------------') 

	XX = []
	YY = []
	YY2 = []
	for i in range(1,1000):
		prob = random.random()/2
		XX.append(prob)
		numm = prob
		LL = y[0]*(numm-x[1])*(numm-x[2])*(numm-x[3])/((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3]))+y[1]*(numm-x[0])*(numm-x[2])*(numm-x[3])/((-x[0]+x[1])*(x[1]-x[2])*(x[1]-x[3]))+y[2]*(numm-x[0])*(numm-x[1])*(numm-x[3])/((-x[0]+x[2])*(-x[1]+x[2])*(x[2]-x[3]))+y[3]*(numm-x[0])*(numm-x[1])*(numm-x[2])/((-x[0]+x[3])*(-x[1]+x[3])*(x[3]-x[2]))
		LL2 = math.cos(5*numm-9)
		YY.append(LL)
		YY2.append(LL2)

	import matplotlib.pyplot as plt
	plt.scatter(XX,YY, c = 'blue', alpha = 1, label = 'Math function')
	plt.scatter(XX,YY2, c = 'red', alpha = 1, label = 'Lagrange fuction')
	plt.title('Lagrange fuction vs math')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend(loc = 'lower right')
	plt.style.use('ggplot')
	plt.grid(True)
	plt.show()
	
print('----------------Create by Lysyi Pavlo KM-71--------------') 	
print('Hello, this programm is create for runs a Interpolation - Newton polynomial and Lagrange fuction on cos(5x-9) in coordinate 0.15')
print('Enter 1 to use Newton and 2 to use Lagrange')
count = input()

try:
    count = int(count)
except ValueError:
    print('Enter a number')

if(count == 1):
	first()
if(count == 2):
	second()