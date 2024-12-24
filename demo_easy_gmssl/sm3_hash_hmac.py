#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:52:54

from __future__ import annotations

import random

from easy_gmssl import EasySM3Digest, EasySM3Hmac
from easy_gmssl.gmssl import SM3_HMAC_MAX_KEY_SIZE

test = EasySM3Digest()
# 计算哈希
plain1 = 'hello,world'.encode('utf-8')
plain2 = '1234567890'.encode('utf-8')
plain3 = (plain1 + plain2)
print('plain hex:', plain3.hex())
test.UpdateData(plain3)
hash_value_2, hash_len, length2 = test.GetHash()
print('hash value:', hash_value_2.hex())
print('hash value length in bytes:', hash_len)

# 计算HMAC
plain = 'hello,world'.encode('utf-8')
print('plain hex:', plain.hex())
key = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MAX_KEY_SIZE)])
print('key hex:', key.hex())
test = EasySM3Hmac(key)
test.UpdateData(plain)
hmac_hex, hmac_len, plain_len = test.GetHmac()
print('hmac value:', hmac_hex.hex(), 'hmac len:', hmac_len, 'plain len:', plain_len)
