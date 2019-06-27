import numpy as np

def BottomUpCutRod(p,n):

    """
    动态规划
    :param p: 价格
    :param n: 长度
    """
    r = [-1] * (n+1)
    s = [-1] * (n+1)
    r[0] = 0
    s[0] = 0
    q = -1

    for j in range(1,n+1):
        for i in range(1,j+1):
            if q < (p[i] + r[j-i]):
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q

    return r, s

if __name__=='__main__':

    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    r,s = BottomUpCutRod(p,10)
    print(r)
    print(s)