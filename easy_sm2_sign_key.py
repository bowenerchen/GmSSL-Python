#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time: 2024-12-23 15:18:18

from __future__ import annotations

from enum import Enum
from typing import Tuple

from pyasn1.codec.der import decoder, encoder
from pyasn1.type import namedtype, univ

from .gmssl import SM2_DEFAULT_ID, SM2_MAX_SIGNATURE_SIZE, Sm2Signature
from .easy_sm2_key import EasySm2Key


# 定义 SM2 签名 ASN.1 结构
class SM2_RS_ASN1_Signature(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('r', univ.Integer()),
        namedtype.NamedType('s', univ.Integer())
    )


class SignatureMode(Enum):
    RS_ASN1 = 'RS_ASN1'
    RS = 'RAW_RS'


def __parse_sm2_rs_asn1_signature__(signature: bytes) -> Tuple[bytes, bytes]:
    if len(signature) > SM2_MAX_SIGNATURE_SIZE:
        raise ValueError('invalid sm2 signature, maximum limit size:{}'.format(SM2_MAX_SIGNATURE_SIZE))
    try:
        decoded, _ = decoder.decode(signature, asn1Spec = SM2_RS_ASN1_Signature())
        r_int = int(decoded['r'])
        r_bytes = r_int.to_bytes(length = 32, byteorder = 'big')
        s_int = int(decoded['s'])
        s_bytes = s_int.to_bytes(length = 32, byteorder = 'big')
    except Exception as e:
        raise ValueError('invalid RS_ASN1 signature:{}'.format(e))
    else:
        return r_bytes, s_bytes


def __encode_rs_to_asn1_sequence__(rs_bytes: Tuple[bytes, bytes]) -> bytes:
    try:
        r_bytes = rs_bytes[0]
        s_bytes = rs_bytes[1]
        r_int = int.from_bytes(r_bytes, byteorder = 'big')
        s_int = int.from_bytes(s_bytes, byteorder = 'big')
    except Exception as e:
        raise ValueError('invalid rs bytes:{}'.format(e))
    else:
        signature = SM2_RS_ASN1_Signature()
        signature.setComponentByName('r', r_int)
        signature.setComponentByName('s', s_int)
        encoded_signature = encoder.encode(signature)
        return encoded_signature


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

    def GetSignValue(self, signature_mode: SignatureMode = SignatureMode.RS_ASN1) -> bytes:
        if not self._sm2_raw_key.has_private_key():
            raise ValueError('empty sm2 private key, cannot do sign')
        if not isinstance(signature_mode, SignatureMode):
            raise ValueError('invalid signature mode:{}'.format(signature_mode))
        ret = self._raw_sign_key.sign()
        if signature_mode == SignatureMode.RS:
            rs_bytes = __parse_sm2_rs_asn1_signature__(ret)
            assert len(rs_bytes) == 2
            assert len(rs_bytes[0]) == 32
            assert len(rs_bytes[1]) == 32
            return rs_bytes[0] + rs_bytes[1]
        return bytes(ret)


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

    def VerifySignature(self, signature_data: bytes, signature_mode: SignatureMode = SignatureMode.RS_ASN1) -> bool:
        if not self._sm2_raw_key.has_public_key():
            raise ValueError('empty sm2 public key, cannot do signature verify')
        if not isinstance(signature_mode, SignatureMode):
            raise ValueError('invalid signature mode:{}'.format(signature_mode))
        if signature_mode == SignatureMode.RS_ASN1:
            if len(signature_data) > SM2_MAX_SIGNATURE_SIZE:
                raise ValueError(
                    'invalid RS_ASN1 signature size, maximum size limited to:{}, current size:{}'.format(SM2_MAX_SIGNATURE_SIZE,
                                                                                                         len(signature_data)))
        if signature_mode == SignatureMode.RS:
            if len(signature_data) != 64:
                raise ValueError('invalid RS mode signature, current length is:{}'.format(len(signature_data)))
            signature_data = __encode_rs_to_asn1_sequence__((signature_data[:32], signature_data[32:]))
        return self._raw_sign_key.verify(signature_data)
