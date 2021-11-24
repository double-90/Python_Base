# -*- coding:utf-8 -*-


from mydict import Dict
import unittest


class TestDict(unittest.TestCase):      # 类名已说明了一切，这个类就是用来测试Dict类的
    def test_init(self):        
        d = Dict(a=1, b='test')         
        self.assertEqual(d.a, 1)        # 这里可以通过属性的形式访问dict中的值，主要是因为Dict类中定义的__getattr__方法
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):                 # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 让每个测试方法调用前后打印出setUp...和tearDown...

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# unittest.TestCase提供了很多内置的条件判断

# self.assertEqual(abs(-1), 1)     断言函数返回的结果与1相等

# with self.assertRaises(KeyError):    断言抛出指定类型的Error

if __name__ == '__main__':
    unittest.main(verbosity=2)


# 脚本文件(命令行输入命令)

# python -m unittest testcode.py