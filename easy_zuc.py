#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-23 18:59:33

from __future__ import annotations

from .gmssl import Zuc, ZUC_IV_SIZE, ZUC_KEY_SIZE


class EasyZuc(object):
    def __init__(self, key: bytes, iv: bytes):
        """
        祖冲之密码算法(ZU Cipher, ZUC)是一种序列密码，密钥和IV长度均为16字节。
        作为序列密码ZUC可以加密可变长度的输入数据，并且输出的密文数据长度和输入数据等长
        因此适合不允许密文膨胀的应用场景
        """
        if len(key) != ZUC_KEY_SIZE:
            raise ValueError('invalid key size:{}, required:{}'.format(len(key), ZUC_KEY_SIZE))
        if len(iv) != ZUC_IV_SIZE:
            raise ValueError('invalid iv size:{}, required:{}'.format(len(iv), ZUC_IV_SIZE))
        self._zuc_ = Zuc(key, iv)

    def Update(self, data: bytes):
        try:
            ret = bytes(self._zuc_.update(data))
        except Exception as e:
            raise ValueError('zuc process error:{}'.format(e))
        else:
            return bytes(ret)

    def Finish(self):
        try:
            ret = bytes(self._zuc_.finish())
        except Exception as e:
            raise ValueError('zuc process error:{}'.format(e))
        else:
            return bytes(ret)
