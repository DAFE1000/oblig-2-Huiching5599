import numpy as np
import matplotlib.pyplot as plt

#function
def f(x):
    return np.exp (-x/4)* np.arctan(x)

#Linkningen vi skal løse
def g(x): 
    return np.arctan(x)-4/(x**2+1)

#deriverte
def dg(x):
    return 1/(x**2+1) + 8*x/ (x**2 +1)**2

#newtons metode
x =2.0
for i in range(5):
    x = x-g(x)/dg(x)

#toppunkt
x_top= x
y_top = f(x)

print("Toppunkt: ")
print("x = ", round(x_top,4))
print ("f(x) =", round(y_top,4))

#plott
xs = np.linspace (-2,8,500)
ys= f(xs)

plt.plot(xs,ys)
plt.scatter(x_top,y_top)
plt.grid()
plt.show()

plt.savefig("plott.png")
print("ok,save pic")



