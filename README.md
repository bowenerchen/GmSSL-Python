# EasyGmssl-Python

## 一、概述

EasyGmSSL  FORK 自开源软件 [GmSSL](https://github.com/guanzhi/GmSSL)，EasyGmSSL旨在为开发者提供一套接口更加友好的国密算法应用开发工具。它涵盖了SM2、SM3、SM4等国密算法的核心功能，并针对实际使用场景中的痛点进行了针对性改进。

## 二、特色功能

1. **便捷安装**
    - 在通过pip安装本SDK时，具备自动编译底层C库的能力，并且会智能地将编译好的二进制文件精准安装到SDK的pip安装目录下，避免对系统路径造成污染，确保了安装过程的简洁性与独立性，让您无需繁琐的手动配置即可快速上手。
    
2. **SM2增强功能**
    - **密钥加解密模式多样化**
      新增了多种SM2密钥加解密模式选择，包括C1C3C2、C1C3C2_ASN1、C1C2C3、C1C2C3_ASN1。这些模式为不同应用需求提供了更灵活的加密策略，无论是在对加密效率有要求，还是对加密数据格式兼容性有考量的场景下，都能找到合适的解决方案。
      
    - **签名验签模式扩展**：在SM2签名验签时，增加了RS_ASN1、RS两种模式选择，适应不同的签名规范和验证场景，使签名验签操作更加贴合实际业务需求。
      
      ![image-20241223193812128](./.README.assets/image-20241223193812128.png)
      
    - **密钥读取便捷化**：允许用户轻松读取SM2公钥、私钥的十六进制明文，方便在调试、密钥管理等环节快速获取关键信息，提升开发效率。
    
3. **基础算法优化**
   对于SM4和SM3以及随机数生成部分，虽然核心算法基于底层库，但在接口层着重增加了参数说明。这使得即使是初次接触国密算法的开发者，也能迅速理解每个参数的含义与用途，降低了开发门槛，加速项目开发进程。

## 三、安装指南

只需在命令行中执行以下pip命令即可完成安装：

```bash
pip install [sdk名称]
```

安装过程中，系统会自动处理底层C库的编译与安装事宜，您只需耐心等待片刻，待安装完成后即可开启国密算法开发之旅。

## 四、使用示例

1. **SM2密钥加解密**
    - 输出多种模式下的密文：
   ```python
       enc = EasySm2EncryptionKey()
       enc.load_sm2_private_key('./test_keys/tmp_test_sm2_private.pem', '123456')
       plain = 'hello,world'
       for mode in SM2CipherMode:
           print(mode, '密文 in Hex:', enc.Encrypt('hello,world'.encode('utf-8'), mode, SM2CipherFormat.HexStr))
   
   ```
2. **SM2公钥、私钥读取**
   ```python
   enc = EasySm2EncryptionKey()
   print('随机生成的公钥数据:', enc.get_sm2_public_key_in_hex())
   print('随机生成的私钥数据:', enc.get_sm2_private_key_in_hex())
   print('公钥 XY 坐标:', enc.get_point_in_hex())
   ```
3. **SM2签名验签**
    - 以RS_ASN1模式为例：
   ```python
   signer_id = 'test_signer'
   print('signer_id hex:', signer_id.encode('utf-8').hex())
   # 初始化用于签名验签的 SM2 密钥
   test = EasySM2SignKey(signer_id = signer_id, pem_private_key_file = './test_keys/tmp_test_sm2_private.pem',
                             password = '123456')
   plain = bytes([random.randint(0, 255) for _ in range(0, 64)])
   print('plain hex:', plain.hex())
   print('private key hex:', test.get_sm2_private_key_in_hex())
   print('public key hex:', test.get_sm2_public_key_in_hex())
   
   # 计算签名
   test.UpdateData(plain)
   # 知情签名值模式为 RS 模式，可选 RS、RS_ASN1
   sign_value = test.GetSignValue(signature_mode = SignatureMode.RS)
   print('signature hex:', sign_value.hex())
   
   # 初始化用于验证签名的 SM2 密钥
   verify_test = EasySM2VerifyKey(signer_id = signer_id, pem_public_key_file = './test_keys/tmp_test_sm2_public.pem')
   # 验证签名
   verify_test.UpdateData(plain)
   # 验证签名时同样指定签名值格式为 RS 模式
   ret = verify_test.VerifySignature(sign_value, signature_mode = SignatureMode.RS)
   
   ```

## 五、注意事项

1. 在使用SM2密钥加解密、签名验签等功能时，请务必根据实际需求谨慎选择合适的模式，不同模式在数据格式、兼容性等方面存在差异。
2. 对于读取的公钥、私钥十六进制明文，要妥善保管，防止泄露，因为这是加密体系的核心机密信息。
3. 虽然SDK尽力优化了接口，但国密算法涉及密码学专业知识，在开发高安全性应用时，建议开发者深入了解相关算法原理，确保应用的安全性。
