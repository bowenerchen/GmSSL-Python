#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:47:27

from __future__ import annotations

from easy_gmssl import EasySm2EncryptionKey, SM2CipherFormat, SM2CipherMode

enc = EasySm2EncryptionKey()
plain = 'hello,world'
# 遍历当前支持的所有 SM2 加解密算法模式
# 当前支持的模式包括：
# C1C3C2_ASN1、C1C3C2、C1C2C3_ASN1、C1C2C3
for mode in SM2CipherMode:
    print(mode, '密文 in Hex:', enc.Encrypt('hello,world'.encode('utf-8'), mode, SM2CipherFormat.HexStr))
