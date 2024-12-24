#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 09:48:59

from __future__ import annotations

from easy_gmssl import EasySm2Key

test = EasySm2Key()
print('公钥数据 In Hex:', test.get_sm2_public_key_in_hex())
print('私钥数据 In Hex:', test.get_sm2_private_key_in_hex())
