#! -*- coding:utf-8 -*-

class Student():
    __slots__ = ("_name", "_age")       # 限制绑定属性

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property                           # 把方法变成属性调用
    def age(self):      
        return self._age

    @age.setter
    def age(self, n):
        if not isinstance(n, int):
            raise TypeError("score must be integer")
        if n < 0 or n > 100:
            raise ValueError("score must between 0 and 100")
        self._age = n
    

s = Student("王丹", 18)

print(s.age)                            # 这里实则是使用了函数 setter 类型的 age()

s._age = 17                             # 这里实则是使用了函数 getter 类型的 age()

print(s.age)
