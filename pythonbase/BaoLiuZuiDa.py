'''
给定一个十进制的正整数number，
选择从里面去掉一部分数字，希望
保留下来的数字组成的正整数最大
'''

def main():
    str = ''.join(input("输入一串数字：").split())
    delnum = int(input("需要删除的个数："))
    l = list(str)
    l.sort()
    for i in range(delnum, len(str)):
        print(l[i])

if __name__ == '__main__':
    main()