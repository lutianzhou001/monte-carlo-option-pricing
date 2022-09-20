# 这是一个示例 Python 脚本。
import numpy as np
import scipy.stats as st
from scipy.stats import norm
from py_vollib.black_scholes import black_scholes as bs

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
r = 0.055
S = 1500
B1 = 1400
B2 = 1800
sigma = 0.80
K1 = 1300
K2 = 1000000000000000000000000
T = 13/365


def n(x):
    return st.norm.cdf(x)


def getd(S, K1, K2, B, r, sigma, T):
    d2 = (np.log(S / K1) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d3 = (np.log(S / B) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d4 = (np.log(B / K2) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d21 = (np.log(S / K1) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d31 = (np.log(S / B) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d41 = (np.log(B / K2) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    print(d2, d3, d4, d21, d31, d41)
    return d2, d3, d4, d21, d31, d41

def blackScholes(r, S, K, T, sigma, type="c"):
    print("calculating Black Scholes")
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "c":
            price = S * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * norm.cdf(d2, 0.0, 1.0)
        elif type == "p":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0.0, 1.0) - S * norm.cdf(-d1, 0.0, 1.0)
        print(price, bs(type, S, K, T, r, sigma))
    except:
        print("Please confirm the option type, either 'c' or 'p'")


def getM(S, K1, K2, B, r, sigma, T):
    SB = (S / B) ** (-(1 - 2 * r / sigma ** 2))
    SB1 = (S / B) ** (1 - 2 * r / sigma ** 2)
    P = (2 * r - sigma ** 2) * T / (sigma * np.sqrt(T))
    P1 = (2 * r + sigma ** 2) * T / (sigma * np.sqrt(T))
    BS = 2 * np.log(B / S) / (sigma * np.sqrt(T))
    return SB, SB1, P, P1, BS


def barrierOptionPricing(S, K1, K2, B, r, sigma, T):
    (d2, d3, d4, d21, d31, d41) = getd(S, K1, K2, B, r, sigma, T)
    (SB, SB1, P, P1, BS) = getM(S, K1, K2, B, r, sigma, T)
    V = S * (n(-d31) - SB * n(d31 - P1) - n(-d2) + SB * n(-d21 - BS)) - K1 * np.exp(-r * T) * (n(-d3) - SB1 * n(d3 - P) - n(-d2) + SB1 * n(-d2 - BS))
    print(V)
    return V



print("NOW PRICING")
Barrier1 = barrierOptionPricing(S, K1, K2, B1, r, sigma, T)
Barrier2 = barrierOptionPricing(S, K1, K2, B2, r, sigma, T)
print(Barrier2 - Barrier1)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
