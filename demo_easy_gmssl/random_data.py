#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:54:41

from __future__ import annotations

from easy_gmssl import EasyRandomData, RandomMode

# 生成随机字节流
test = EasyRandomData()
ret = test.GetRandomData(20)
print(ret.hex())
# 生成随机字符串
test = EasyRandomData(mode = RandomMode.RandomStr)
ret = test.GetRandomData(64)
print(ret)
