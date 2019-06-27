def jianshengzi(n):
    # 先对边界问题进行求解，因为明显剪的值小于不剪的值
    # 则提出先讨论这三种情况
    if n < 2:
        return 0
    if n == 2:
        return 1    #长度为2，只能剪成1*1
    if n == 3:
        return 2    #长度为3，剪成2*1 > 1*1*1

    #若绳子长于４呢,申请一个长度为50的数组
    #罗列出切割的边界问题

    h = [0] * (n+1)
    h[0] = 0
    h[1] = 1
    h[2] = 2
    h[3] = 3
    # 递归问题是 f(n) = max{f(i)*f(n-i)}
    for i in range(4,n+1):
        maxs = 0
        for j in range(1,i//2+1):
            mult = h[j] * h[i-j]
            if maxs < mult:
                maxs = mult
            h[i] = maxs     # 每次J的迭代轮询出该长度的最大值
    return h[n]

print(jianshengzi(9))
