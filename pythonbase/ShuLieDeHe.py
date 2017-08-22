'''
输入数据有多组，每组占一行，由两个整数n
（n < 10000）和m(m < 1000)组成，n和m的含义如前所述。
对于每组输入数据，输出该数列的和，
每个测试实例占一行，要求精度保留2位小数。
'''

import math

def main():
    i = int(input("输入第一项数为："))
    j = int(input("求前几项的平方根和："))
    a = [0] * j
    sum = 0
    for k in range(0, j):
        a[k] = math.sqrt(i)
        i = math.sqrt(i)
    for k in range(0, j):
        sum += a[k]
    print(round(sum, 2))
if __name__ == "__main__":
    main()


