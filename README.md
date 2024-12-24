# EasyGmssl-Python

## 一、概述

EasyGmSSL  FORK 自<u>**北京大学 GUNAZHI 老师团队的开源国密算法库**</u>： [GmSSL](https://github.com/guanzhi/GmSSL)，EasyGmSSL旨在为开发者提供一套接口更加友好的国密算法应用开发工具。它涵盖了SM2、SM3、SM4等国密算法的核心功能，并针对实际使用场景中的痛点进行了针对性改进。

此 SDK 的 git 地址为：https://github.com/bowenerchen/GmSSL-Python

## 二、特色功能

1. **便捷安装**
    - 在通过pip安装本SDK时，具备自动编译底层C库的能力，并且会智能地安装编译好的二进制文件，避免对系统路径造成污染，确保了安装过程的简洁性与独立性，让您无需繁琐的手动配置即可快速上手。
    
2. **SM2增强功能**
    - **密钥加解密模式多样化**
      新增了多种SM2密钥加解密模式选择，包括C1C3C2、C1C3C2_ASN1、C1C2C3、C1C2C3_ASN1。这些模式为不同应用需求提供了更灵活的加密策略，无论是在对加密效率有要求，还是对加密数据格式兼容性有考量的场景下，都能找到合适的解决方案。
      
    - **签名验签模式扩展**
      在SM2签名验签时，增加了RS_ASN1、RS两种模式选择，适应不同的签名规范和验证场景，使签名验签操作更加贴合实际业务需求。
      
    - **密钥读取便捷化**
      允许用户轻松读取SM2公钥、私钥的十六进制明文，方便在调试、密钥管理等环节快速获取关键信息，提升开发效率。
    
3. **基础算法优化**
   
   对于SM4和SM3以及随机数生成部分，虽然核心算法基于底层库，但在接口层着重增加了参数说明。这使得即使是初次接触国密算法的开发者，也能迅速理解每个参数的含义与用途，降低了开发门槛，加速项目开发进程。

## 三、安装指南

只需在命令行中执行以下pip命令即可完成安装：

```bash
pip install easy_gmssl
```

安装过程中，系统会自动处理底层C库的编译与安装事宜，待编译安装完成后即可开启国密算法开发之旅。

## 四、使用示例

1. **SM2密钥加解密**
   - 输出多种模式下的密文：
   ```python
   from __future__ import annotations
   
   from easy_gmssl import EasySm2EncryptionKey, SM2CipherFormat, SM2CipherMode
   
   enc = EasySm2EncryptionKey()
   plain = 'hello,world'
   # 遍历当前支持的所有 SM2 加解密算法模式
   # 当前支持的模式包括：
   # C1C3C2_ASN1、C1C3C2、C1C2C3_ASN1、C1C2C3
   for mode in SM2CipherMode:
       print(mode, '密文 in Hex:', enc.Encrypt('hello,world'.encode('utf-8'), mode, SM2CipherFormat.HexStr))
   ```

2. **SM2公钥、私钥读取**
   ```python
   from __future__ import annotations
   
   from easy_gmssl import EasySm2Key
   
   test = EasySm2Key()
   print('公钥数据 In Hex:', test.get_sm2_public_key_in_hex())
   print('私钥数据 In Hex:', test.get_sm2_private_key_in_hex())
   ```

3. **SM2签名验签**

   - 以RS_ASN1模式为例：
   ```python
   from __future__ import annotations
   
   import random
   
   from easy_gmssl import EasySM2SignKey, EasySM2VerifyKey, SignatureMode
   
   signer_id = 'test_signer'
   print('signer_id hex:', signer_id.encode('utf-8').hex())
   # 初始化用于签名验签的 SM2 密钥，此时不需要关心签名值的模式
   test = EasySM2SignKey(signer_id = signer_id, pem_private_key_file = './test_keys/tmp_test_sm2_private.pem',
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
   verify_test = EasySM2VerifyKey(signer_id = signer_id, pem_public_key_file = './test_keys/tmp_test_sm2_public.pem')
   # 验证签名
   verify_test.UpdateData(plain)
   # 验证签名时同样指定签名值格式为 RS 模式
   ret = verify_test.VerifySignature(sign_value, signature_mode = SignatureMode.RS)
   ```

4.   **SM4对称加解密示例**

     ```python
     from __future__ import annotations
     
     from easy_gmssl import EasySm4CBC
     from easy_gmssl.gmssl import SM4_BLOCK_SIZE, SM4_CBC_IV_SIZE
     
     key = 'x' * SM4_BLOCK_SIZE
     iv = 'y' * SM4_CBC_IV_SIZE
     
     test_cbc_enc = EasySm4CBC(key.encode('utf-8'), iv.encode('utf-8'), True)
     plain1 = 'hello,world'
     plain2 = '1234567890'
     cipher1 = test_cbc_enc.Update(plain1.encode('utf-8'))
     cipher2 = test_cbc_enc.Update(plain2.encode('utf-8'))
     ciphers = cipher1 + cipher2 + test_cbc_enc.Finish()
     
     test_dec = EasySm4CBC(key.encode('utf-8'), iv.encode('utf-8'), False)
     decrypted_plain1 = test_dec.Update(ciphers)
     decrypted_plain = decrypted_plain1 + test_dec.Finish()
     
     print('解密成功：', decrypted_plain == (plain1 + plain2).encode('utf-8'))
     ```

5.   **SM3 HASH 与 HMAC 示例**

     ```python
     from __future__ import annotations
     
     import random
     
     from easy_gmssl import EasySM3Digest, EasySM3Hmac
     from easy_gmssl.gmssl import SM3_HMAC_MAX_KEY_SIZE
     
     test = EasySM3Digest()
     
     plain1 = 'hello,world'.encode('utf-8')
     plain2 = '1234567890'.encode('utf-8')
     plain3 = (plain1 + plain2)
     print('plain hex:', plain3.hex())
     test.UpdateData(plain3)
     hash_value_2, hash_len, length2 = test.GetHash()
     print('hash value:', hash_value_2.hex())
     print('hash value length in bytes:', hash_len)
     
     
     plain = 'hello,world'.encode('utf-8')
     print('plain hex:', plain.hex())
     key = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MAX_KEY_SIZE)])
     print('key hex:', key.hex())
     test = EasySM3Hmac(key)
     test.UpdateData(plain)
     hmac_hex, hmac_len, plain_len = test.GetHmac()
     print('hmac value:', hmac_hex.hex(), 'hmac len:', hmac_len, 'plain len:', plain_len)
     ```

6.   **随机数生成示例**

     ```python
     from __future__ import annotations
     from easy_gmssl import EasyRandomData, RandomMode
     test = EasyRandomData()
     ret = test.GetRandomData(20)
     print(ret.hex())
     test = EasyRandomData(mode = RandomMode.RandomStr)
     ret = test.GetRandomData(64)
     print(ret)
     ```

     

7.   **ZUC 加解密示例**

     ```python
     from __future__ import annotations
     
     from easy_gmssl import EasyRandomData, EasyZuc
     from easy_gmssl.gmssl import ZUC_IV_SIZE, ZUC_KEY_SIZE
     
     # 生成密钥与 IV
     key = EasyRandomData().GetRandomData(ZUC_KEY_SIZE)
     iv = EasyRandomData().GetRandomData(ZUC_IV_SIZE)
     # 加密操作
     test = EasyZuc(key, iv)
     plain1 = 'hello,world'.encode('utf-8')
     cipher1 = test.Update(plain1)
     plain2 = '1234567890'.encode('utf-8')
     cipher2 = test.Update(plain2)
     cipher3 = test.Finish()
     
     # 解密操作
     test2 = EasyZuc(key, iv)
     ret1 = test2.Update(cipher1)
     ret2 = test2.Update(cipher2)
     ret3 = test2.Update(cipher3)
     ret4 = test2.Finish()
     assert ret1 + ret2 + ret3 + ret4 == plain1 + plain2
     print('解密成功：', ret1 + ret2 + ret3 + ret4 == plain1 + plain2)
     ```

     

## 五、注意事项

1. 在使用SM2密钥加解密、签名验签等功能时，请务必根据实际需求谨慎选择合适的模式，不同模式在数据格式、兼容性等方面存在差异。
2. 对于读取的公钥、私钥十六进制明文，要妥善保管，防止泄露，因为这是加密体系的核心机密信息。
3. 虽然SDK尽力优化了接口，但国密算法涉及密码学专业知识，在开发高安全性应用时，建议开发者深入了解相关算法原理，确保应用的安全性。
