'''
对于每个测试实例，要求输出所有在给定范围内的水仙花数，
就是说，输出的水仙花数必须大于等于m,并且小于等于n，
如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开;
如果给定的范围内不存在水仙花数，则输出no;
每个测试实例的输出占一行。
'''


def main():
    num = int(input("Enter a number: "))
    i = int(num / 100)
    j = num % 10 % 10
    k = int((num/10)) % 10
    if pow(i,3) + pow(j, 3) + pow(k, 3) == num:
        print("水仙花数：%d" %num )
    else:
        print("非水仙花数")

if __name__ == "__main__":
    main()