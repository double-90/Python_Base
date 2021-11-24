# -*- coding:utf-8 -*-


class Dict(dict):
    '''
    Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
    
    example

    >>> d = Dict()
    >>> d['x'] = 10
    >>> d.x
    10

    >>> d.y = 20
    >>> d['y']
    20

    >>> d1 = Dict(x=100, y=200, z='3')
    >>> d1.z
    '3'


    >>> d1['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'

    >>> d1.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        # super(Dict, self).__init__(**kw)      python2的写法
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, val):
        self[key] = val


if __name__ == '__main__':
    import doctest
    doctest.testmod()


# 脚本文件（通过命令行去调用）

# python mydict2.py     (没有输出则证明编写的doctest没问题，即只有错误的时候会输出错误信息)
