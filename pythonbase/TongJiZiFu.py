'''
求出一串字符串中最先出现三次的字符
'''


def main():
    str = ''.join(input().split())
    for i in range(len(str)):
        s = str[i]
        if s.isalpha():
            num = str[0:i+1].count(s)
            if num == 3:
                print(s)
                break

if __name__ == "__main__":
    main()
