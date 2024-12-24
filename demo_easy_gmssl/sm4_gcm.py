#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:51:29

from __future__ import annotations

from easy_gmssl import EasySm4GCM
from easy_gmssl.gmssl import SM4_BLOCK_SIZE, SM4_CBC_IV_SIZE, SM4_GCM_DEFAULT_TAG_SIZE

key = 'x' * SM4_BLOCK_SIZE
iv = 'y' * SM4_CBC_IV_SIZE
# 定义拓展验证数据，加解密时此数据需要保持一致
aad = 'a' * (SM4_BLOCK_SIZE + SM4_CBC_IV_SIZE)
# 定义tag长度，最小 8 个字节
tag_len = int(SM4_GCM_DEFAULT_TAG_SIZE / 2)
test_gcm_enc = EasySm4GCM(key.encode('utf-8'), iv.encode('utf-8'), aad, tag_len, True)
plain1 = 'hello,world'
plain2 = '1234567890'
# 进行加密操作
cipher1 = test_gcm_enc.Update(plain1.encode('utf-8'))
cipher2 = test_gcm_enc.Update(plain2.encode('utf-8'))
ciphers = cipher1 + cipher2 + test_gcm_enc.Finish()
# GCM模式下的密文长度与明文长度等长
# 返回的密文中包含了 tag 长度
print('ciphers len:', len(ciphers), 'tag_len=', tag_len, 'plain len:', len(plain1 + plain2))

# 进行解密操作，此时aad和tag_len需要与加密时保持一致
test_dec = EasySm4GCM(key.encode('utf-8'), iv.encode('utf-8'), aad, tag_len, False)
decrypted_plain1 = test_dec.Update(ciphers)
decrypted_plain = decrypted_plain1 + test_dec.Finish()

print('解密成功：', decrypted_plain == (plain1 + plain2).encode('utf-8'))
