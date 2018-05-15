""" 函数练习 """
# coding=utf-8


class Person(object):

    # 类属性
    address = 'sz'

    def __init__(self, name, gender, birth, color, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        # 私有属性带有前缀__
        self.__color = color
        # 属性值可以是动态变化的
        for k, v in kw.items():
            setattr(self, k, v)

    # 通过方法获取私有属性值
    def get_color(self):
        return self.__color

    # 定义类方法
    @classmethod
    def get_address(cls):
        return cls.address


if __name__ == "__main__":
    xm = Person('xiaoming', 'male', '1991-01-01', 'whtie')
    xh = Person('xiaohong', 'Femal', '1992-02-02', 'black', job='Student')

    # 类属性改变，实例访问属性也会改变
    Person.address = 'bj'

    # 实例改变属性值不会影响其它类属性的值
    xm.address = 'gz'
    print(xh.get_address())
