# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

from sqlalchemy import create_engine, MetaData

def upper_attr(future_class_name, future_class_parents, future_class_attr):

    """返回一个类对象，将属性都转换为大写形式"""
    # 选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过type来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr # 这会作用到这个模块中的所有类

class Foo(metaclass=upper_attr):
    __metaclass__ = upper_attr
    bar = 'bip'

print(dir(Foo))
print(hasattr(Foo, 'bar'))
print(Foo.__mro__)
