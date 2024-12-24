#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-23 14:10:41

from __future__ import annotations

from typing import Tuple

from .gmssl import Sm3, SM3_DIGEST_SIZE, SM3_HMAC_MAX_KEY_SIZE, SM3_HMAC_MIN_KEY_SIZE, SM3_HMAC_SIZE, Sm3Hmac


class EasySM3Digest(object):
    """
    EasySM3Digest 对象非线程安全，同一个对象不可并发执行写操作
    """

    def __init__(self):
        self._raw_sm3_key = Sm3()
        self._data_length: int = 0

    def UpdateData(self, data: bytes):
        self._raw_sm3_key.update(data)
        self._data_length += len(data)

    def Reset(self):
        self._raw_sm3_key.reset()
        self._data_length = 0

    def GetHash(self) -> Tuple[bytes, int, int]:
        """
        返回：哈希十六进制串、哈希值长度、明文数据长度
        """
        hash_bytes = self._raw_sm3_key.digest()
        assert len(hash_bytes) == SM3_DIGEST_SIZE
        return hash_bytes, len(hash_bytes), self._data_length


class EasySM3Hmac(object):
    def __init__(self, key: bytes):
        if len(key) > SM3_HMAC_MAX_KEY_SIZE:
            raise ValueError('invalid key, maximum key size limit to:{} bytes'.format(SM3_HMAC_MAX_KEY_SIZE))
        if len(key) < SM3_HMAC_MIN_KEY_SIZE:
            raise ValueError('invalid key, minimum key size required at least:{} bytes'.format(SM3_HMAC_MIN_KEY_SIZE))
        self._raw_sm3_hmac = Sm3Hmac(key)
        self._key: bytes = key
        self._plain_length: int = 0

    def UpdateData(self, data: bytes):
        self._raw_sm3_hmac.update(data)
        self._plain_length += len(data)

    def Reset(self):
        self._raw_sm3_hmac.reset(self._key)
        self._plain_length = 0

    def GetHmac(self) -> Tuple[bytes, int, int]:
        """
        返回：HMAC十六进制字符串、HMAC值长度、明文数据长度
        """
        hmac_bytes = self._raw_sm3_hmac.generate_mac()
        assert len(hmac_bytes) == SM3_HMAC_SIZE
        return hmac_bytes, len(hmac_bytes), self._plain_length
