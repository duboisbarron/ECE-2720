#!/usr/bin/env python
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt


def logistic_map(r, x, n):
    if n == 0:
        return x
    # print(r*x*(1-x))
    return logistic_map(r, r*x*(1-x), n-1)


def make_plot(r, x_0, figNum):
    x = np.zeros(31)
    x[0] = x_0
    for i in range(30):
        x[i+1] = r*x[i]*(1-x[i])

    # print(x)
    plt.plot(range(31), x)
    plt.xlabel('Iteration')
    plt.ylabel('State')
    plt.title('Evolution for r = ' + str(r) + ' and x0 = ' + str(x_0) + '')
    plt.savefig('figure' + str(figNum))
    plt.clf()

def make_plot2(rVals, x_0):

    title = 'Evolution for x0 = ' + str(x_0) + ' and r = ' + str(rVals)
    for r in rVals:
        # title = title + 'R = ' + str(r) + ', '
        arr = np.zeros(31)
        arr[0] = x_0
        for i in range(30):
            arr[i+1] = r * arr[i] * (1 - arr[i])

        plt.plot(range(31), arr, label='R = ' + str(r))
        plt.legend()
    plt.xlabel('Iteration')
    plt.ylabel('State')
    plt.title(title)
    plt.savefig('figure2')
    plt.clf()

def sweep_r_values(x_0):
    rVals = np.linspace(start=0, stop=4, num=1000)
    # print(rVals[-1])
    convergingArr = []

    for r in rVals:
#         compute 1000 iterations and test whether the sequence converges
        arr = np.zeros(1001)
        arr[0] = x_0
        for i in range(1000):
            arr[i + 1] = r * arr[i] * (1 - arr[i])
        if arr[-1] < 0.000001 or abs(arr[-1] - arr[-2])/arr[-1] < 0.001:
            convergingArr.append(1)
            # print(r)
        else:
            convergingArr.append(0)
    # print(convergingArr)


    plt.bar(rVals, convergingArr, width=0.00001, color='green', edgecolor='green', align='edge', linewidth=1)
    plt.xlim([0.0, 4.01])
    plt.xlabel('R Value')
    plt.ylabel('Does R Value Converge?')
    plt.yticks(np.arange(2), ('Does not converge', 'Converges'), fontsize=6, rotation=45)
    plt.title('Convergence Test for R Values in [0.0, 4.0]')
    plt.savefig('figure7')
    plt.clf()


def make_plot8(x_0):
    rVals = np.linspace(start=0, stop=4, num=1000)
    #         compute 1000 iterations for each r value
    limits = []
    r_minus_one_over_rs = []
    for r in rVals:
        if r != 0:
            r_minus_one_over_rs.append((r-1)/r)
            # print (r-1)/r
        else:
            r_minus_one_over_rs.append(0)
        arr = np.zeros(1001)
        arr[0] = x_0
        for i in range(1000):
            arr[i + 1] = r * arr[i] * (1 - arr[i])
#         if the sequence converges for a particular value of r, let f(r) denote the limit
        if arr[-1] < 0.000001 or abs(arr[-1] - arr[-2])/arr[-1] < 0.001:

            if r <= 1:

                limits.append(0)
            else:
                limits.append((r-1)/r)
        else:
            # print('does not converge')
            limits.append(-0.25)
            # print('did not converge')

    # have limis and r_minus_one_over_rs
    plt.plot(rVals, limits, label= 'Limits')
    plt.plot(rVals, r_minus_one_over_rs, label='(r-1)/r')
    plt.legend()
    plt.xlabel('R Value')
    plt.ylabel('Function Value')
    plt.ylim([-3, 3])
    plt.title('F(r) and (r-1)/r for r values in [0.0, 4.0]')
    plt.savefig('figure8')
    plt.clf()



make_plot(0.5, 0.5, 1)
make_plot2([0.5, 0.25, 0.9], 0.5)
make_plot(1.5, 0.5, 3)
make_plot(2.5, 0.5, 4)
make_plot(3.25, 0.5, 5)
make_plot(3.75, 0.5, 6)
sweep_r_values(0.5)
make_plot8(0.5)



