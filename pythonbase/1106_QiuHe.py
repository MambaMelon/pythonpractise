'''
输入n,m两个整数，求得1到n中相加和为m的组合数
'''

'''
def rec(i, m, res):
    ans = []
    for j in range(i, n+1):
        if j == m:
            ans.extend([x+[j] for x in res])
            break
        if j < m:
            ans.extend(rec(j+1, m-j, [x+[j] for x in res]))
        else:
            continue
    return ans

if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    ans = rec(1, m, [[]])
    for i in  ans:
        print(i)
'''



def f(n, m, l, k):
    if m == 0:
        print(' '.join(l))
    for i in range(k, n):
        if i > m:
            break
        l.append(str(i))
        f(n, m-i, l, i+1)
        l.pop()

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))
    li = []
    f(n, m, li, 1)