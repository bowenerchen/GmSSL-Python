#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:55:13

from __future__ import annotations

from easy_gmssl import EasyRandomData, EasyZuc
from easy_gmssl.gmssl import ZUC_IV_SIZE, ZUC_KEY_SIZE

# 生成密钥与 IV
key = EasyRandomData().GetRandomData(ZUC_KEY_SIZE)
iv = EasyRandomData().GetRandomData(ZUC_IV_SIZE)
# 加密操作
test = EasyZuc(key, iv)
plain1 = 'hello,world'.encode('utf-8')
cipher1 = test.Update(plain1)
plain2 = '1234567890'.encode('utf-8')
cipher2 = test.Update(plain2)
cipher3 = test.Finish()

# 解密操作
test2 = EasyZuc(key, iv)
ret1 = test2.Update(cipher1)
ret2 = test2.Update(cipher2)
ret3 = test2.Update(cipher3)
ret4 = test2.Finish()
assert ret1 + ret2 + ret3 + ret4 == plain1 + plain2
print('解密成功：', ret1 + ret2 + ret3 + ret4 == plain1 + plain2)
