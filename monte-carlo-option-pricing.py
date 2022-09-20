import datetime
import numpy
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import random
from scipy.stats import norm

# initial derivative parameters
S = 1600  # stock price
K = 1300  # strike price
B1 = 1400  # barrier price
B2 = 1800  # barrier price
vol = 0.80  # volatility
r = 0.055  # risk-free rate
Step = 1000  # number of time steps
M = 5000  # number of simulations
# market_value = 3.86  # market price of option
T = 13 / 365  # time in years

# Precompute constants
dt = T / Step
nudt = (r - 0.5 * vol ** 2) * dt
volsdt = vol * np.sqrt(dt)
lnS = np.log(S)
po = 0
pb = 0
pw = 0
# Standard Error Placeholders
# sum_CT = 0
# sum_PT = 0
# sum_CT2 = 0
# sum_PT2 = 0
# Monte Carlo Method
# fig, ax = plt.subplots()  # 创建图实例
# fig = plt.figure()  # 定义新的三维坐标轴
# ax3 = plt.axes(projection='3d')

N = norm.cdf


def d2(S, K, T, r, sigma):
    return (np.log(S / K) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def binary_call(S, K, T, r, sigma, Q=1):
    N = norm.cdf
    return np.exp(-r * T) * N(d2(S, K, T, r, sigma)) * Q


def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r * T) * N(d2)


sumRevenue = 0
for i in range(M):
    print(i)
    # print(i)
    lnSt = lnS
    col = (np.random.random(), np.random.random(), np.random.random())
    x = []
    y = []
    for j in range(Step):
        lnSt = lnSt + nudt + volsdt * np.random.normal()
        St = np.exp(lnSt)
        if St > B2:
            # pass
            break
        if St < B1:
            # pass
            break
        x.append(j)
        y.append(St)
    ST = np.exp(lnSt)
    if ST > B2:
        # print("knock out!")
        revenue = 0
        sumRevenue = sumRevenue + revenue
        # sum_CT2 = sum_CT2 + revenue * revenue
    elif ST < B1:
        # print("knock out!")
        revenue = 0
        sumRevenue = sumRevenue + revenue
        # sum_CT2 = sum_CT2 + revenue * revenue
    else:
        # print("now st is larger than b")
        revenue = np.exp(-r * T) * max(0, ST - K)
        # print(revenue)
        sumRevenue = sumRevenue + revenue
    plt.plot(x, y, c=col)  # s-:方形
    # print("company average revenue".format(np.round(revenue0, 2)))
    # plt.scatter(r, revenue0)
    # plt.plot(r, revenue0, color='b', zorder=2)
    # Compute Expectation and SE
    # C0 = np.exp(-r * T) * sum_CT / M
    # P0 = np.exp(-r * T) * sum_PT / M
    # sigmaCT = np.sqrt((sum_CT2 - sum_CT * sum_CT / M) * np.exp(-2 * r * T) / (M - 1))
    # sigmaPT = np.sqrt((sum_PT2 - sum_PT * sum_PT / M) * np.exp(-2 * r * T) / (M - 1))
    # SECT = sigmaCT / np.sqrt(M)
    # SEPT = sigmaPT / np.sqrt(M)
print(sumRevenue / M)
plt.title(str(M) + "times simulation in pricing barrier options")
plt.show()
