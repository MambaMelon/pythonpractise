'''
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，
形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …,
yyyw, yyyx, yyyy 其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，
输入是任意一个编码，输出这个编码对应的Index.

如：baca   则对应的编码为16331
'''
def coding(s):
    le = len(s)
    index  = 0
    bit1 = 25**3 + 25**2 + 25 + 1
    bit2 = 25**3 + 1
    bit3 = 25 + 1
    bit4 = 1
    b = [bit1, bit2, bit3, bit4]
    for i in range(0, le):
        index += b[i]*(ord(s[i])-ord('a'))
    return index+(le-1)

while True:
    try:
        s = input()
        print(coding(s))
    except:
        break

if __name__ == "__main__":
    coding(s)