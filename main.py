# -*- coding: utf-8 -*

import matplotlib.pyplot as plt
import numpy as np

def line_calcul (m,b,x):
    return m*x+b

def average (a,b):
    return (a+b)/2

data = [
        [-2,-3],
        [-1,-1],
        [1,2],
        [4,3],

        ]

#initialisation
x_y = 0
x = 0
x_2 = 0
y = 0

list_x = []
list_y = []
list_y_new =[]
SCE_D = 0
SCE_Y = 0
##################
for row in data:
    x_y += row[0]*row[1]
    x+=row[0]
    y+=row[1]
    x_2+=pow(row[0],2)
    list_x.append(row[0])
    list_y.append(row[1])

sum_x_y = float(x_y)/len(data)
sum_x = float(x)/len(data)
sum_y = float(y)/len(data)
sum_x_2 = float(x_2)/len(data)

#clacul de a et b y = mx + b

m = ((sum_x_y)-(sum_x*sum_y))/(sum_x_2-pow(sum_x,2))
b = sum_y - (m*sum_x)
print ("y = %.2f*x + %.2f"%(m,b))

for row in data:
    y_calcule = line_calcul(m,b,row[0])
    list_y_new.append(y_calcule)
    SCE_D += pow(row[1]-y_calcule,2)
    SCE_Y += pow((row[1]-sum_y),2)

print(SCE_D)
print(SCE_Y)
#coef de determination

R_2 = 1-(SCE_D/SCE_Y)
print(R_2)


#figure
x = np.linspace(-10, 10, 100)
plt.plot(x, m*x+b,color="red", label='linear')


plt.scatter(list_x,list_y,marker='x')
plt.title('Regression')
plt.show()
