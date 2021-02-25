
from __future__ import print_function

from functools import wraps


def log(*args, **kwargs):
    def _log(func):
        print("log init %s args:%s kwargs:%s" % (func.__name__, args, kwargs))

        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            func(*func_args, **func_kwargs)

        return wrapper
    return _log


@log("a", "b", a=1, b=2, c=3)
def test1():
    print('test1 ..')


@log()
def test2(a):
    print('test2 .. %s' % a)


test1()
test2('a')


'''
log init args:('a', 'b') kwargs:{'a': 1, 'c': 3, 'b': 2}
_log init test1
log init args:() kwargs:{}
_log init test2
'''
