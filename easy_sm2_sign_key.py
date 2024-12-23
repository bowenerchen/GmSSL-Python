#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-23 15:18:18

from __future__ import annotations

from Core.gmssl import SM2_DEFAULT_ID, Sm2Signature
from easy_sm2_key import EasySm2Key


class EasySM2SignKey(EasySm2Key):
    def __init__(self, signer_id: str = SM2_DEFAULT_ID, pem_private_key_file: str = '', password = ''):
        super().__init__()
        try:
            self.load_sm2_private_key(pri_key_file = pem_private_key_file, password = password)
        except Exception:
            raise ValueError('load sm2 private key in pem format failed:{}, password:{}'.format(pem_private_key_file, password))
        else:
            self._raw_sign_key = Sm2Signature(sm2_key = self._sm2_raw_key, signer_id = signer_id, sign = True)

    def UpdateData(self, data: bytes):
        if not self._sm2_raw_key.has_private_key():
            raise ValueError('empty sm2 private key, cannot do sign')
        self._raw_sign_key.update(data)

    def GetSignValue(self) -> bytes:
        if not self._sm2_raw_key.has_private_key():
            raise ValueError('empty sm2 private key, cannot do sign')
        return bytes(self._raw_sign_key.sign())


class EasySM2VerifyKey(EasySm2Key):
    def __init__(self, signer_id: str = SM2_DEFAULT_ID, pem_public_key_file: str = ''):
        super().__init__()
        try:
            self.load_sm2_pub_key(pem_public_key_file)
        except Exception:
            raise ValueError('invalid sm2 public key in pem format:{}'.format(pem_public_key_file))
        else:
            self._raw_sign_key = Sm2Signature(sm2_key = self._sm2_raw_key, signer_id = signer_id, sign = False)

    def UpdateData(self, data: bytes):
        if not self._sm2_raw_key.has_public_key():
            raise ValueError('empty sm2 public key, cannot do verify')
        self._raw_sign_key.update(data)

    def VerifySignature(self, signature_data: bytes) -> bool:
        if not self._sm2_raw_key.has_public_key():
            raise ValueError('empty sm2 public key, cannot do signature verify')
        return self._raw_sign_key.verify(signature_data)
