#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConstError, "Can't change const.{name}".format(name=key)

        if not key.isupper():
            raise self.ConstCaseError, "const name {name} is not all uppercase".format(name=key)

        self.__dict__[key] = value

import sys
sys.modules[__name__] = _const()
