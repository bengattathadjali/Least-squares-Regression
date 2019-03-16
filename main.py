# -*- coding: utf-8 -*
import matplotlib.pyplot as plt

data = [
        [2,3],
        [1,2],
        [5,3],
        [4,5],
        ]


x_y = 0
x = 0
x_2 = 0
y = 0

list_x = []
list_y = []

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

plt.scatter(list_x,list_y,marker='x')
plt.ylabel('Regression')
plt.show()
