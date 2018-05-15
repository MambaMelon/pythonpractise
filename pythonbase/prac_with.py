""" with关键字 """
# coding=utf-8


def add_list(alist):
    for i in alist:
        yield i + 1

def h():
    print("to be...")
    yield 5
    print("number!")

if __name__ == "__main__":
    oldList = (1, 2, 3, 4)
    li = add_list(oldList)

    c = h()
    c.__next__()