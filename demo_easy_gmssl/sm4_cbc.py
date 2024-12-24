#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:49:46

from __future__ import annotations

from easy_gmssl import EasySm4CBC
from easy_gmssl.gmssl import SM4_BLOCK_SIZE, SM4_CBC_IV_SIZE

key = 'x' * SM4_BLOCK_SIZE
iv = 'y' * SM4_CBC_IV_SIZE
# 加密操作
test_cbc_enc = EasySm4CBC(key.encode('utf-8'), iv.encode('utf-8'), True)
plain1 = 'hello,world'
plain2 = '1234567890'
cipher1 = test_cbc_enc.Update(plain1.encode('utf-8'))
cipher2 = test_cbc_enc.Update(plain2.encode('utf-8'))
ciphers = cipher1 + cipher2 + test_cbc_enc.Finish()

# 解密操作
test_dec = EasySm4CBC(key.encode('utf-8'), iv.encode('utf-8'), False)
decrypted_plain1 = test_dec.Update(ciphers)
decrypted_plain = decrypted_plain1 + test_dec.Finish()

print('解密成功：', decrypted_plain == (plain1 + plain2).encode('utf-8'))
