# -*- coding: utf-8 -*
import csv
import matplotlib.pyplot as plt
import numpy as np

def line_calcul (m,b,x):
    return m*x+b

def average (a,b):
    return (a+b)/2



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
compt = 0
##################

with open('data.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter=',')
    for row in reader:
        x_y += float(row[0])*float(row[1])
        x+=float(row[0])
        y+=float(row[1])
        x_2+=pow(float(row[0]),2)
        list_x.append(float(row[0]))
        list_y.append(float(row[1]))
        compt += 1


    

sum_x_y = float(x_y)/compt
sum_x = float(x)/compt
sum_y = float(y)/compt
sum_x_2 = float(x_2)/compt

#clacul de a et b y = mx + b

m = ((sum_x_y)-(sum_x*sum_y))/(sum_x_2-pow(sum_x,2))
b = sum_y - (m*sum_x)
print ("y = %.2f*x + %.2f"%(m,b))

with open('data.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter=',')
    for row in reader:
        y_calcule = line_calcul(m,b,float(row[0]))
        list_y_new.append(y_calcule)
        SCE_D += pow(float(row[1])-y_calcule,2)
        SCE_Y += pow((float(row[1])-sum_y),2)

print(SCE_D)
print(SCE_Y)
#coef de determination

R_2 = 1-(SCE_D/SCE_Y)
print(R_2)


#figure
x = np.linspace(-10, 30, 100)
plt.plot(x, m*x+b,color="red", label='linear')


plt.scatter(list_x,list_y,marker='x')
plt.title('Regression')
plt.show()
