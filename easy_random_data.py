#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-23 17:00:50

from __future__ import annotations

import random
import string
from enum import Enum
from typing import Union

import gmssl


class RandomMode(Enum):
    RandomBytes = 'RandomBytes'
    RandomStr = 'RandomStr'


class EasyRandomData(object):
    _all_random_characters_ = list(string.ascii_letters + string.digits + "'\"{}[]\\!@#$%^&*()_+|:")

    def __init__(self, mode: RandomMode = RandomMode.RandomBytes):
        self._mode = mode

    def GetRandomData(self, length: int = 16) -> Union[bytes | str]:
        r = gmssl.rand_bytes(length)
        if length < 1:
            raise ValueError('invalid random length, required greater than 0')
        if self._mode == RandomMode.RandomBytes:
            return r
        elif self._mode == RandomMode.RandomStr:
            random.shuffle(self._all_random_characters_)
            result = ""
            for i in r:
                result += self._all_random_characters_[int(i) % len(self._all_random_characters_)]
            return result
