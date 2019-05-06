# -*- coding: utf-8 -*-


def log(level, *args, **kwargs):
    # * 无名字的参数
    # ** 有名字的参数
    def inner(func):
        def wrapper(*args, **kwargs):
            print level, 'before calling ', func.__name__
            print level, 'args', args, 'kvargs', kwargs
            func(*args, **kwargs)
            print level, 'end calling ', func.__name__

        return wrapper

    return inner


# @log
# def hello():
#     print 'hello'


@log(level='INFO')
def hello(name, age):
    print 'hello ', name, age


if __name__ == '__main__':
    hello('world', age=2)
