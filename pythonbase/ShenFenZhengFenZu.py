
def main():
    str = input("输入身份证号: ").replace(" ","")
    length = len(str)
    if length == 6:
        print(str)
    elif length > 6 and length <=14:
        print(str[0:6] + " " + str[6:length])
    elif length>14 and length<=18:
        print(str[0:6] + " " + str[6:14] + " " + str[14:length])
    else:
        print("输入的身份证号不合法")

if __name__ == "__main__":
    main()