# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 上午11:15
# @Author  : chaos
# @FileName: prototype_1.py
# @Software: PyCharm
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass