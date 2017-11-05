'''
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，
并输出结果。输入值小于1000。如，输入为10, 程序应该输出结果为2。
（共有两对质数的和为10,分别为(5,5),(3,7)）
'''
def main():
    num = int(input("输入一个整数"))
    count = 0
    for i in range(1, num//2):
        if i%2 == 0 and (num-i)%2 == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()