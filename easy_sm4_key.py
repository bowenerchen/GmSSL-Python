#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-23 17:23:36

from __future__ import annotations

from enum import Enum

from .gmssl import SM4_BLOCK_SIZE, SM4_CBC_IV_SIZE, SM4_GCM_DEFAULT_TAG_SIZE, Sm4Cbc, Sm4Gcm


class EncryptionMode(Enum):
    CBCMode = 'CBC'
    GCMMode = 'GCM'
    CTRMode = 'CTR'


class EasySm4CBC(object):
    def __init__(self, key: bytes, iv: bytes, do_encrypt: bool = True):
        """
        key 和 iv 的长度必须为 16 字节
        """
        if len(key) != SM4_BLOCK_SIZE:
            raise ValueError('invalid key length:{}, required:{}'.format(len(key), SM4_BLOCK_SIZE))
        if len(iv) != SM4_CBC_IV_SIZE:
            raise ValueError('invalid iv length:{}, required:{}'.format(len(key), SM4_CBC_IV_SIZE))
        self._sm4_cbc_ = Sm4Cbc(key, iv, do_encrypt)
        self._do_encryption = do_encrypt
        if self._do_encryption:
            self._action_ = 'sm4 cbc encryption'
        else:
            self._action_ = 'sm4 cbc decryption'

    def Update(self, data: bytes) -> bytes:
        """
        返回的 bytes 数据需要累加
        """
        try:
            ret = self._sm4_cbc_.update(data)
        except Exception as e:
            raise ValueError('{} failed:{}'.format(self._action_, e))
        else:
            return bytes(ret)

    def Finish(self) -> bytes:
        """
        返回的 bytes 数据需要累加作为最终的密文或者明文
        """
        try:
            ret = self._sm4_cbc_.finish()
        except Exception as e:
            raise ValueError('{} failed:{}'.format(self._action_, e))
        return bytes(ret)


class EasySm4GCM(object):
    def __init__(self, key: bytes, iv: bytes, aad: bytes = b'', tag_len: int = SM4_GCM_DEFAULT_TAG_SIZE, do_encrypt: bool = True):
        """
        key 和 iv 的长度必须为 16 字节
        tag_len 值最小为 8，最长为 16
        """
        if len(key) != SM4_BLOCK_SIZE:
            raise ValueError('invalid key length:{}, required:{}'.format(len(key), SM4_BLOCK_SIZE))
        if len(iv) != SM4_CBC_IV_SIZE:
            raise ValueError('invalid iv length:{}, required:{}'.format(len(key), SM4_CBC_IV_SIZE))
        if tag_len < SM4_GCM_DEFAULT_TAG_SIZE / 2 or tag_len > SM4_GCM_DEFAULT_TAG_SIZE:
            raise ValueError(
                'invalid tag_len:{}, required:[{},{}]'.format(
                    tag_len, int(SM4_GCM_DEFAULT_TAG_SIZE / 2), SM4_GCM_DEFAULT_TAG_SIZE))
        self._sm4_gcm_ = Sm4Gcm(key, iv, aad, tag_len, do_encrypt)
        self._do_encryption = do_encrypt
        if self._do_encryption:
            self._action_ = 'sm4 gcm encryption'
        else:
            self._action_ = 'sm4 gcm decryption'

    def Update(self, data: bytes) -> bytes:
        """
        返回的 bytes 数据需要累加
        """
        try:
            ret = self._sm4_gcm_.update(data)
        except Exception as e:
            raise ValueError('{} failed:{}'.format(self._action_, e))
        else:
            return bytes(ret)

    def Finish(self) -> bytes:
        """
        返回的 bytes 数据需要累加作为最终的密文或者明文
        """
        try:
            ret = self._sm4_gcm_.finish()
        except Exception as e:
            raise ValueError('{} failed:{}'.format(self._action_, e))
        return bytes(ret)
