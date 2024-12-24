#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-24 10:48:31

from __future__ import annotations

import random

from easy_gmssl import EasySM2SignKey, EasySM2VerifyKey, SignatureMode

signer_id = 'test_signer'
print('signer_id hex:', signer_id.encode('utf-8').hex())
# 初始化用于签名验签的 SM2 密钥，此时不需要关心签名值的模式
test = EasySM2SignKey(signer_id = signer_id, pem_private_key_file = '../test_keys/tmp_test_sm2_private.pem',
                      password = '123456')
plain = bytes([random.randint(0, 255) for _ in range(0, 64)])
print('plain hex:', plain.hex())
print('private key hex:', test.get_sm2_private_key_in_hex())
print('public key hex:', test.get_sm2_public_key_in_hex())

# 计算签名
test.UpdateData(plain)
# 指定签名值模式为 RS 模式，可选 RS、RS_ASN1
sign_value = test.GetSignValue(signature_mode = SignatureMode.RS)
print('signature hex:', sign_value.hex())

# 初始化用于验证签名的 SM2 密钥
verify_test = EasySM2VerifyKey(signer_id = signer_id, pem_public_key_file = '../test_keys/tmp_test_sm2_public.pem')
# 验证签名
verify_test.UpdateData(plain)
# 验证签名时同样指定签名值格式为 RS 模式
ret = verify_test.VerifySignature(sign_value, signature_mode = SignatureMode.RS)
