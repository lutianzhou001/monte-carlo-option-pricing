# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import math
from sympy import *


sigma = 0.80
r = 0.055
q = 0
T = 13/365
K = 1300
S = 1600
U = 1400
L = 1800
l= math.log(U/L)


alpha = -1/sigma**2 * (r-q-1/2*sigma**2)
beta = -r - 1/2*sigma**2 * (r-q-1/2*sigma**2)

total = 0
for n in range(1, 10000000000):
    A = 2/l * math.sin(n*math.pi/l*math.log(S/L)) * math.exp(-n**2*math.pi*sigma**2/2/l**2*T)
    print(A)
    S = symbols('S')
    B = integrate(S, (S, U, L))
    print(B)
    # B = integrate(math.pow(S/L,-alpha) * (1-K/S) *math.sin(n*math.pi/l*math.log(S/L)), (S, U, L))
    total = total + A * B
    print(total)
V = total * (S/L)**alpha * math.exp(beta*T)


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
