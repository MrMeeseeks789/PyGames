from game2 import make_PC_guess_num
import random
import matplotlib.pyplot as plt
import numpy as np

print("Welcome to Number Matcher! Play to test your Computer's LUCK")
# x = int(input("Select a level : "))
x_axis = []
y_axis = []
for x in range(10, 2000, 10):
    # iter = int(input("Select number of iterations : "))
    iter = 1000
    g = random.randrange(1, x)
    att = []
    for i in range(iter):
        att.append(make_PC_guess_num(x,g))
    avg_att = sum(att) / iter
    x_axis.append(x)
    y_axis.append(avg_att)
    # print(f"**** {avg_att} average attempts **** taken to guess on {x} level after {iter} iterations")
n_x = np.arange(1, 2000)
n_y = 1.26*(np.log2(n_x))

plt.plot(x_axis, y_axis)
plt.plot(n_x, n_y)
plt.show()