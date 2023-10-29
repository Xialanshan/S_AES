# S_AES
## 测试报告

#### 前言

GUI主界面设计：

![image](https://github.com/Xialanshan/S_AES/assets/110965468/62974b3e-1228-4c2b-830b-6f82fd07fe5b)

<p align="center">图1 GUI主界面</p>

Test Mode : 进入基础的测试界面

![image](https://github.com/Xialanshan/S_AES/assets/110965468/3077a96c-2857-4c79-ab0f-bc58895386f7)

<p align="center">图2 Test Mode 界面</p>

Work Mode : 进入CBC工作模式

![image](https://github.com/Xialanshan/S_AES/assets/110965468/e1884b94-8d8b-4a4d-9eca-499312e0d431)

<p align="center">图3 Work Mode 界面</p>

Multi Mode : 进入多重加密模式

![image](https://github.com/Xialanshan/S_AES/assets/110965468/27d4d08f-2e12-469c-ae4b-1a7cda856464)

<p align="center">图4 Multi Mode 界面</p>


#### 第一关：基础测试（Test Mode）
<a name="第一关-基础测试test-mode"></a>

| 格式要求    | message     | key     |
| ------- | ------- | ------- |
| Binary   | len = 16 * N   | 16-bit 二进制  |
| Hex   | len = 4 * N   | 4位 16进制  |
| ASCII   | len = 2 * N   | 16-bit 二进制  |

不满足上述对应要求的时候，会弹出提示窗口，说明正确的格式，并要求重新输入，示例如图（图5，图6，仅展示部分）：

![image](https://github.com/Xialanshan/S_AES/assets/110965468/bed1982f-555f-4f86-8bf6-a54c8a519b05)

<p align="center">图5 message 格式不符合要求，弹出提示</p>

![image](https://github.com/Xialanshan/S_AES/assets/110965468/947e5b9a-ebc4-4dcd-a566-1b063263db1d)

<p align="center">图6 key 格式不符合要求，弹出提示</p>


1. Binary加解密测试

   测试明文：1010101010101010    测试密文：1011101111100110

   密钥：1000010101010101

   生成密文：1011101111100110    生成明文：1010101010101010

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/a31023ac-33c8-4825-bf52-57a6ab2f498c">
   
   <p align="center">图7 二进制加密</p>
   
   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/8a8c2704-7b82-4349-9e4f-048330db98c2">
   
   <p align="center">图8 二进制解密</p>
   
   测试明文与生成密文一致，测试密文与生成密文一致，加解密成功。

2. Hex加解密测试

   测试明文：1234    测试密文：ab86

   密钥：abcd

   生成密文：ab86    生成明文：1234

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/0b337406-6cd2-443f-814b-13dd585c7230">

   <p align="center">图9 十六进制加密</p>
   
   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/9d117f3a-beca-4c5d-bcfe-0b0a1ab3e4cb">

   <p align="center">图10 十六进制解密</p>

   测试明文与生成密文一致，测试密文与生成密文一致，加解密成功。

3. ASCII加解密
   
   测试明文：AQ    测试密文：=÷

   密钥：1001110101010110

   生成密文：=÷    生成明文：AQ

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/eea067ae-edf9-465a-b982-bb6e8f03832f">

   <p align='center'>图11 ASCII加密</p>
   
   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/e8a26f15-21c0-45ee-8d27-5ddd50fd95bb">

   <p align='center'>图12 ASCII解密</p>

   测试明文与生成密文一致，测试密文与生成密文一致，加解密成功。


#### 第二关 交叉测试

1. 二进制加解密测试
   
   ![bc685eb8e788f730535b364febf5645](https://github.com/Xialanshan/S_AES/assets/110965468/9cac0832-7ed3-48e4-93f4-32659b7043af)

   ![bb0e58b52a268611a0c7f054b02e807](https://github.com/Xialanshan/S_AES/assets/110965468/325b3fb0-1263-4153-bd1f-4b36e253b9b0)

   我组进行加密，其他组进行解密，最终结果显示，二进制加解密交叉测试通过。

2. ASCII加解密测试

   ![31ace30555c71bca51acf5541f6e1c8](https://github.com/Xialanshan/S_AES/assets/110965468/04af153e-0369-4b0f-93e0-70407d198a68)

   ![0b1b379aafe04a999c5fa65ff46ee84](https://github.com/Xialanshan/S_AES/assets/110965468/4e783342-b5b8-4701-bc75-b340ada904af)

   用相同的密钥加密相同的明文，两组得到的密文一致，ASCII加解密交叉测试通过

3. 双重加解密测试

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/6390ebcc-e89e-453d-a389-d45da66e4032">

   ![8079e8d77c1d874298a925cff410709](https://github.com/Xialanshan/S_AES/assets/110965468/efa3414b-0997-4910-9be7-3d884ca073d0)

   我组进行加密，其他组进行解密，最终结果显示，双重加解密交叉测试通过。

4. 三重加解密测试

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/5b0d6b01-0cb4-4a2d-9d2f-546320342edf">
   
   ![7716d6790b47a08bfef2ce8b64a892e](https://github.com/Xialanshan/S_AES/assets/110965468/966ba644-4a9f-47d0-b99e-a412ba37ba05)

   我组进行加密，其他组进行解密，最终结果显示，三重加解密交叉测试通过。

   
#### 第三关 拓展功能
具体测试在[基础测试](#第一关基础测试test-mode)中已经展示，此处不再赘述


#### 第四关 多重加密

| 格式要求    | message     | key     |
| ------- | ------- | ------- |
| Double en-decryption   | len = 16   | 32-bit 二进制  |
| Three en-decryption   | len = 16  | 32 16进制  |

1. 双重加解密
   
   测试明文：1001010101110001    测试密文：1111000011001011

   密钥：11110000101010010001101010101001

   生成密文：1111000011001011    生成明文：1001010101110001

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/944ed5cf-2809-4756-bde0-8fa35bbe4cab">

   <p align='center'>图 双重加密</p>

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/94190f92-ddc3-493f-b37b-a7674958efdd">

   <p align='center'>图 双重解密</p>

   测试明文与生成密文一致，测试密文与生成密文一致，加解密成功。

2. 三重加解密

   测试明文：1001010101110001    测试密文：1001111000011010

   密钥：111100001010100100011010101010010011001010101110

   生成密文：1001111000011010    生成明文：1001010101110001

   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/5308c6e0-7fab-4893-ade5-45076cacda75">
   
   <p align='center'>图 三重加密</p>
   
   <img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/02450f0b-5a44-4ad8-ae31-7b4b40354d5f">
   
   <p align='center'>图 三重解密</p>

   测试明文与生成密文一致，测试密文与生成密文一致，加解密成功。

3. 中间相遇攻击

   | 明文| 0000111100001111| 1111111100000000| 1100110011001101 | 
   | ----| ------- | ------- | ---------|
   | 密文| 1110010001011110|0010010001010010| 1010101100100010|

   密钥设置：<img width="161" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/ff8e0be2-38c0-41bf-bc0a-c1f0bdaa4667">

   <img width="234" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/c8ea304f-b919-4d48-9337-2c1b14381ab7">

   返回结果 == key1 + key2


#### 第五关 CBC工作模式
```
工作模式下：
   加密时，系统支持输入任意长度的二进制字符串明文，默认使用末尾补0填充，不支持更改填充方式，返回加密结果和加密时填充的位数(用以解密)；
   解密时，如果不输入填充位数padding，默认未填充，否则请输入明文加密时填充的位数，否则不能返回正确的解密明文。
   密钥要求是16-bit二进制字符串。
   初始向量通过系统随机生成，系统内置随机数种子seed=12345。
```
测试明文：1000111100100000010101010101      测试密文：00010010110000100101100001010000   (padding = 4)

密钥：1110010001011110

生成密文：00010010110000100101100001010000   生成明文：1000111100100000010101010101

<img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/e6840b68-7803-473d-a5e3-562bafc601b9">

<p align='center'>图 CBC加密</p>

<img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/d1f669e1-3dc2-40ba-98e0-d07d6fe7f894">

<p align='center'>图 CBC解密</p>

测试明文与生成密文一致，测试密文与生成密文一致，加解密成功。

当密文分组被篡改时，以测试密文为例，调转两个分组的排序，篡改后的密文为：01011000010100000001001011000010，其余保持不变，解密结果为：1001001010010111000000100111

<img width="1120" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/bc8e7b6e-b007-4b79-9b49-85255a55c6a5">

<p align='center'>图 CBC解密篡改测试</p>

两次生成的明文不一致，说明密文被篡改后无法得到正确的明文。


## 开发手册
#### 1. 固定参数

S盒：<img width="168" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/18a16da9-d723-424d-aef1-d7bd22530090">

逆S盒：<img width="181" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/9d52291d-e106-4b29-83ea-c0045cea4716">

列混淆矩阵：<img width="101" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/c9de8aa3-95bf-469f-92b9-bb139a050c64">

逆列混淆矩阵：<img width="128" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/18425bf6-994a-41d5-bd20-1c0b8025270d">

#### 2. 密钥拓展
1. 按位异或函数：输入二进制串a、b，输出a与b按位异或后的结果
   ```python
   def xor_bits(a, b):
    """
    按位异或
    :param a: 二进制数
    :param b: 二进制数
    :return: a与b异或的结果
    """
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
   ```
2. 半字节交换函数：输入8bit二进制，输出前4bit与后4bit交换后的结果
   ```python
   def RotNib(w):
    """
    半字节交换
    :param w: 8bits二进制串
    :return: 交换后的8bits
    """
    left_half = w[:4]
    right_half = w[4:]
    result = right_half + left_half
    return result
   ```
3. 半字节替换函数：输入8bits二进制串，返回经过S盒替换后的8bits
   ```python
   def SubNib(w):
    """
    半字节替换
    :param w: 8bits二进制串
    :return: 替换后的8bits
    """
    left_half = w[:4]
    right_half = w[4:]
    s_left_half = sbox_substitution(left_half, S)
    s_right_half = sbox_substitution(right_half, S)
    result = s_left_half + s_right_half
    return result
   ```
4. S盒替换函数：输入需要替换的4bits二进制与使用的替换盒，返回替换后的4bits二进制数。
   ```python
   def sbox_substitution(input_text, S):
    """
    S盒替换
    :param input_text: 需要替换的4bits二进制
    :param S: 使用的替换盒
    :return: 返回替换后的4bits二进制数
    """
    row = int(input_text[0] + input_text[1], 2)
    col = int(input_text[2] + input_text[3], 2)
    return format(S[row][col], '04b')        # 以二进制格式返回
   ```
5. 轮密钥生成函数：输入16bits母密钥，返回列表形式存储的3个16bits轮密钥
   ```python
   def get_key_extension(w):
    """
    生成轮密钥
    :param w: 16bits母密钥
    :return: 列表形式存储的3个16bits轮密钥
    """
    RCON1 = '10000000'      # 轮常数
    RCON2 = '00110000'
    key_w = []
    w0 = w[:8]
    w1 = w[8:]
    key_w.append(w0+w1)
    w2=xor_bits(xor_bits(w0,RCON1),SubNib(RotNib(w1)))
    w3=xor_bits(w2,w1)
    key_w.append(w2+w3)
    w4=xor_bits(xor_bits(w2,RCON2),SubNib(RotNib(w3)))
    w5=xor_bits(w4,w3)
    key_w.append(w4+w5)
    return key_w
   ```

#### 3. 加解密辅助函数
1. 密钥加函数：同按位异或函数
2. 半字节代替函数：输入16bits明文二进制串，返回半字节替换后的16bits二进制串
   ```python
   def halfbyte_substitution(P, S):
    """
    半字节代替
    :param P: 16bits明文二进制串
    :return: 半字节替换后的16bits二进制串
    """
    halfByte00 = P[:4]
    halfByte10 = P[4:8]
    halfByte01 = P[8:12]
    halfByte11 = P[12:]
    s_halfByte00 = sbox_substitution(halfByte00, S)
    s_halfByte10 = sbox_substitution(halfByte10, S)
    s_halfByte01 = sbox_substitution(halfByte01, S)
    s_halfByte11 = sbox_substitution(halfByte11, S)
    result = s_halfByte00 + s_halfByte10 + s_halfByte01 + s_halfByte11
    return result
   ```
3. 行位移函数：输入16bits二进制串，返回行位移后的16bits二进制串
   ```python
   def shift_row(P):
    """
    行移位
    :param P: 16bits二进制串
    :return: 行位移后的16bits二进制串
    """
    halfByte00 = P[:4]
    halfByte10 = P[4:8]
    halfByte01 = P[8:12]
    halfByte11 = P[12:]
    result = halfByte00 + halfByte11 + halfByte01 + halfByte10
    return result
   ```
4. 列混淆函数：输入列混淆矩阵与16bit二进制串，返回混淆后的16bits二进制串
   ```python
   def confusion_column(P, M):
    """
    列混淆
    :param P: 16bits二进制串
    :param M: 列混淆矩阵
    :return: 混淆后的16bits二进制串
    """
    halfByte00 = P[:4]  
    halfByte10 = P[4:8]
    halfByte01 = P[8:12]
    halfByte11 = P[12:]
    c_halfByte00 = GetKeys.xor_bits((gf2_4_multiply_binary(format(M[0][0], '04b'), halfByte00)).zfill(4),
                            (gf2_4_multiply_binary(format(M[0][1], '04b'), halfByte10)).zfill(4))
    c_halfByte10 = GetKeys.xor_bits((gf2_4_multiply_binary(format(M[1][0], '04b'), halfByte00)).zfill(4),
                            (gf2_4_multiply_binary(format(M[1][1], '04b'), halfByte10)).zfill(4))
    c_halfByte01 = GetKeys.xor_bits((gf2_4_multiply_binary(format(M[0][0], '04b'), halfByte01)).zfill(4),
                            (gf2_4_multiply_binary(format(M[0][1], '04b'), halfByte11)).zfill(4))
    c_halfByte11 = GetKeys.xor_bits((gf2_4_multiply_binary(format(M[1][0], '04b'), halfByte01)).zfill(4),
                            (gf2_4_multiply_binary(format(M[1][1], '04b'), halfByte11)).zfill(4))
    result = c_halfByte00 + c_halfByte10 + c_halfByte01 + c_halfByte11
    return result
   ```
5. 伽罗华有限域乘法计算函数：输入两个二进制串，输出在伽罗华有限相乘的结果
   ```python
   def gf2_4_multiply_binary(a, b):
    """
    GF(2^4)中的多项式乘法函数
    :param a: 二进制串
    :param b: 二进制串
    :return: 模乘后的结果(二进制串)
    """
    # 将二进制字符串转换为整数
    a = int(a, 2)
    b = int(b, 2)

    # 在GF(2^4)中执行乘法
    result = 0
    for i in range(4):
        if (b & 1) == 1:
            result ^= a
        high_bit_set = (a & 8) == 8
        a <<= 1
        if high_bit_set:
            a ^= 0b10011    # GF(2^4)的模
        b >>= 1
    return bin(result)[2:]
   ```

#### 4. 加解密函数
1. 16bits二进制加密函数
   ```python
   def encrypting_binary(plaintext_binary, key):
    """
    对16bits二进制明文加密
    :param plaintext_binary: 16bits二进制明文
    :param key: 16bits母密钥
    :return: 16bits二进制密文
    """
    keys = GetKeys.get_key_extension(key)
    Ak0 = GetKeys.xor_bits(plaintext_binary, keys[0])
    NS = halfbyte_substitution(Ak0, S)
    SR = shift_row(NS)
    MC = confusion_column(SR, M)
    Ak1 = GetKeys.xor_bits(MC, keys[1])
    NS = halfbyte_substitution(Ak1, S)
    SR = shift_row(NS)
    Ak2 = GetKeys.xor_bits(SR, keys[2])
    return Ak2
   ```
2. 16bits二进制解密函数
   ```python
   def decrypting_binary(ciphertext_binary, key):
    """
    对16bits二进制密文解密
    :param ciphertext_binary: 16bits二进制密文
    :param key: 16bits母密钥
    :return: 16bits二进制明文
    """
    keys = GetKeys.get_key_extension(key)
    Ak2 = GetKeys.xor_bits(ciphertext_binary, keys[2])
    ISR = shift_row(Ak2)
    INS = halfbyte_substitution(ISR, S_inv)
    Ak1 = GetKeys.xor_bits(INS, keys[1])
    IMC = confusion_column(Ak1, M_inv)
    ISR = shift_row(IMC)
    INS = halfbyte_substitution(ISR, S_inv)
    Ak0 = GetKeys.xor_bits(INS, keys[0])
    return Ak0
   ```
3. 二进制加密函数
   ```python
   def encrypting_binaryStr(plaintext_str, key):
    """
    长度为16bits(倍数)的二进制明文加密操作
    :param plaintext_str: 16bits(倍数)二进制明文串
    :param key: 16bits母密钥
    :return: 16bits(倍数)二进制密文串
    """
    length = len(plaintext_str)
    if length % 16 != 0:
        return
    ciphertext_binarystring = ""
    for i in range(0, length, 16):
        group = plaintext_str[i:i + 16]
        plain_group = utils.encrypting_binary(group, key)
        ciphertext_binarystring += plain_group
    return ciphertext_binarystring
   ```
4. 二进制解密函数
   ```python
   def decrypting_binaryStr(ciphertext_str, key):
    """
    长度为16bits(倍数)的二进制密文解密操作
    :param ciphertext_str: 16bits(倍数)二进制密文串
    :param key: 16bits母密钥
    :return: 16bits(倍数)二进制明文串
    """
    length = len(ciphertext_str)
    if length % 16 != 0:
        return
    plaintext_binarystring = ""
    for i in range(0, length, 16):
        group = ciphertext_str[i:i + 16]
        plain_group = utils.decrypting_binary(group, key)
        plaintext_binarystring = plaintext_binarystring + plain_group
    return plaintext_binarystring
   ```
5. 十六进制加密函数
   ```python
   def encrypting_hexadecimal(plaintext_hexadecimal, key_hexadecimal):
    """
    :param plaintext_hexadecimal: 十六进制明文
    :param key_hexadecimal: 十六进制密钥
    :return: 十六进制的密文
    """
    length = len(plaintext_hexadecimal)
    if length % 4 != 0:
        return
    ciphertext_hexadeciaml = ""
    key = (bin(int(key_hexadecimal, 16))[2:]).zfill(16)
    for i in range(0, length, 4):
        group = plaintext_hexadecimal[i:i + 4]
        ciphertext_binary = (bin(int(group, 16))[2:]).zfill(16)
        ciphertext_binary = utils.encrypting_binary(ciphertext_binary, key)
        ciphertext_hexadeciaml1 = hex(int(ciphertext_binary, 2))[2:].zfill(4)
        ciphertext_hexadeciaml += ciphertext_hexadeciaml1
    return ciphertext_hexadeciaml
   ```
6. 十六进制解密函数
   ```python
   def decrypting_hexadecimal(ciphertext_hexadecimal, key_hexadecimal):
    """
    密文为十六进制的解密函数
    :param ciphertext_hexadecimal: 十六进制密文
    :param key_hexadecimal: 十六进制密钥
    :return: 十六进制的解密明文
    """
    length = len(ciphertext_hexadecimal)
    if length % 4 != 0:
        return
    plaintext_hexadeciaml = ""
    key = (bin(int(key_hexadecimal, 16))[2:]).zfill(16)
    for i in range(0, length, 4):
        group = ciphertext_hexadecimal[i:i + 4]
        ciphertext_binary = (bin(int(group, 16))[2:]).zfill(16)
        plaintext_binary = utils.decrypting_binary(ciphertext_binary, key)
        plaintext_hexadeciaml1 = hex(int(plaintext_binary, 2))[2:].zfill(4)
        plaintext_hexadeciaml = plaintext_hexadeciaml + plaintext_hexadeciaml1
    return plaintext_hexadeciaml
   ```
7. ASCII加密函数
   ```python
   def encrypting_ascii(plaintext_ascii, key):
    """
    :param plaintext_ascii: ASCII明文
    :param key: 16bits二进制母密钥
    :return: ASCII密文
    """
    length = len(plaintext_ascii)
    if length % 2 != 0:     
        return
    ciphertext_ascii = ""
    for i in range(0, length, 2):
        group = plaintext_ascii[i:i + 2]
        plaintext_binary = ''.join([bin(ord(char))[2:].zfill(8) for char in group])
        ciphertext_binary1 = utils.encrypting_binary(plaintext_binary, key)
        byte1 = ciphertext_binary1[0:8]
        byte2 = ciphertext_binary1[8:16]
        ciphertext_ascii1 = chr(int(byte1, 2)) + chr(int(byte2, 2))
        ciphertext_ascii += ciphertext_ascii1
    return ciphertext_ascii
   ```
8. ASCII 解密函数
   ```python
   def decrypting_ascii(ciphertext_ascii, key):
    """
    ASCII码密文解密
    :param ciphertext_ascii: ASCII码形式的密文
    :param key: 16bits二进制密文
    :return: ASCII码形式的明文
    """
    length = len(ciphertext_ascii)
    if length % 2 != 0:
        return
    plaintext_ascii = ""
    for i in range(0, length, 2):
        group = ciphertext_ascii[i:i + 2]
        ciphertext_binary = ''.join([bin(ord(char))[2:].zfill(8) for char in group])
        plaintext_binary1 = utils.decrypting_binary(ciphertext_binary, key)
        byte1 = plaintext_binary1[0:8]
        byte2 = plaintext_binary1[8:16]
        plaintext_ascii1 = chr(int(byte1, 2)) + chr(int(byte2, 2))
        plaintext_ascii = plaintext_ascii + plaintext_ascii1
    return plaintext_ascii
   ```

#### 5. 多重加解密函数
1. 双重加密函数：输入16bits二进制明文和32bits二进制母密钥，返回16bits二进制密文
   ```python
   def encrypting_double(plaintext_double, key):
    """
    双重加密
    :param plaintext_double: 16bits二进制明文
    :param key: 32bits二进制母密钥
    :return: 16bits密文
    """
    key1 = key[:16]
    key2 = key[16:]
    ciphertext_double = utils.encrypting_binary(utils.encrypting_binary(plaintext_double, key1), key2)
    return ciphertext_double
   ```
3. 双重解密函数：输入16bits二进制密文和32bits二进制母密钥，返回16bits二进制明文
   ```python
   def decrypting_double(ciphertext_double, key):
    """
    双重解密
    :param ciphertext_double: 16bits二进制明文
    :param key: 32bits二进制母密钥
    :return: 16bits明文
    """
    key1 = key[:16]
    key2 = key[16:]
    plaintext_double = utils.decrypting_binary(utils.decrypting_binary(ciphertext_double, key2), key1)
    return plaintext_double
   ```
4. 三重加密函数：输入16bits二进制明文和48bits二进制母密钥，返回16bits二进制密文
   ```python
   def encrypting_three(plaintext_three, key):
    """
    三重加密
    :param plaintext_double: 16bits二进制明文
    :param key: 48bits二进制母密钥
    :return: 16bits二进制密文
    """
    key1 = key[:16]
    key2 = key[16:32]
    key3=key[32:]
    ciphertext=utils.encrypting_binary(utils.decrypting_binary(utils.encrypting_binary(plaintext_three,key1),key2),key3)
    return ciphertext
   ```
6. 三重解密函数：输入16bits二进制密文和48bits二进制母密钥，返回16bits二进制明文
   ```python
   def decrypting_three(ciphertext_three,key):
    """
    三重解密
    :param ciphertext_double: 16bits二进制明文
    :param key: 48bits二进制母密钥
    :return: 16bits明文
    """
    key1 = key[:16]
    key2 = key[16:32]
    key3 = key[32:]
    plaintext = utils.decrypting_binary(utils.encrypting_binary(utils.decrypting_binary(ciphertext_three, key3), key2), key1)
    return plaintext
   ```

#### 6. 中间相遇攻击
1. 第一组加密解密，得到一个可能密钥的列表
   ```python
   def encrypt_decrypt_all(P, C):
    my_list = []  # 记录所有加密结果
    key1_list = []
    key2_list = []
    for key in range(2 ** 16):
        binary_key1 = format(key, '016b')  # 将密钥转换为二进制字符串
        my_list.append(utils.encrypting_binary(P, binary_key1))
    for key in range(2 ** 16):
        binary_key2 = format(key, '016b')
        decrypted_text = utils.decrypting_binary(C, binary_key2)
        if decrypted_text in my_list:
            index = my_list.index(decrypted_text)
            binary_key1 = format(index, '016b')
            key1_list.append(binary_key1)
            key2_list.append(binary_key2)
    return key1_list, key2_list
   ```
2. 其他组明密文对的加解密，找到最终的密钥
   ```python
   def try_decrypt(key1_list, key2_list, p_list, c_list):
    key1 = []
    key2 = []
    for i in range(len(c_list)):
        key1.clear()
        key2.clear()
        for j in range(len(key1_list)):
            decrypt_P = decrypting.decrypting_double(c_list[i], key1_list[j] + key2_list[j])
            if decrypt_P == p_list[i]:
                key1.append(key1_list[j])
                key2.append(key2_list[j])
        key1_list = copy.copy(key1)
        key2_list = copy.copy(key2)
    return key1, key2
   ```
3. 中间相遇攻击函数
   ```python
   def meet_in(P, C):
    key1_list, key2_list = encrypt_decrypt_all(P[0], C[0])
    P_copy = copy.copy(P)
    C_copy = copy.copy(C)
    P_copy.pop(0)
    C_copy.pop(0)
    result_key=[]
    key1_list11,key2_list11=try_decrypt(key1_list, key2_list, P_copy, C_copy)
    for i in range(len(key1_list11)):
        result_key.append(key1_list11[i]+key2_list11[i])
    return result_key
   ```
#### 7. 工作模式
1. 初始向量生成函数
   ```python
   def IV_generate(seed):
    random.seed(seed)
    iv = bytes([random.randint(0, 255) for _ in range(2)])
    iv_binary = ''.join(format(byte, '08b') for byte in iv)
    return iv_binary
   ```
2. CBC加密函数：输入任意长度的二进制明文和16bits母密钥，输出密文和加密过程中填充的位数
   ```python
   def CBC_encryption(plaintext_binary, key, seed, padding):
    """
    CBC加密
    :param plaintext_binary: 任意长度的二进制明文
    :param key: 16bits母密钥
    :param seed: 随机数种子
    :param padding: 前端函数格式要求, padding = 0
    :return: 填充后明文对应长度的二进制密文
    """
    IV = IV_generate(seed)
    result = str()
    plain_group = str()
    if len(plaintext_binary)%16 != 0:
        group_number = len(plaintext_binary)//16 + 1
        padding = group_number * 16 - len(plaintext_binary)
        plaintext_binary += '0' * padding
    for i in range(0, len(plaintext_binary), 16):
        group = plaintext_binary[i:i + 16]
        if i == 0:
            curr = GetKeys.xor_bits(group, IV)      # 第一轮和IV做异或, 再加密
        else:
            curr = GetKeys.xor_bits(group, plain_group)     # 之后先和上一轮加密的结果做异或, 再加密
        plain_group = utils.encrypting_binary(curr, key)
        result += plain_group
    return result, padding
   ```
3. CBC解密函数：输入待解密密文和填充数，输出明文
   ```python
   def CBC_decryption(ciphertext_binary, key, seed, padding):
    """
    CBC解密
    :param ciphertext_binary: 16*N bits的二进制密文
    :param key: 16bits母密钥
    :param seed: 随机数种子
    :return: 填充前的二进制明文
    """
    IV = IV_generate(seed)
    result = str()
    cipher_group = str()
    for i in range(0,len(ciphertext_binary),16):
        group = ciphertext_binary[i: i+16]
        curr = utils.decrypting_binary(group, key)
        if i == 0:
            cipher_group = GetKeys.xor_bits(IV, curr)
            result += cipher_group
        else:
            cipher_group = GetKeys.xor_bits(ciphertext_binary[i-16:i], curr)
            result += cipher_group
    if padding == 0:
        return result
    else:
        return result[:-padding]
   ```

#### 8. GUI界面和用户交互设置
1. 主界面：创建三个接口，分别加载出不同模式的具体界面
   ```javascript
   <body>
    <button id="testModeButton">Test Mode</button>
    <button id="workModeButton">Work Mode</button>
    <button id="multiModeButton">Multi Mode</button>

    <script>
        const testModeButton = document.getElementById("testModeButton");
        const workModeButton = document.getElementById("workModeButton");
        const multiModeButton = document.getElementById("multiModeButton");
        testModeButton.addEventListener("click", function() {
            window.location.href = "/test_mode";
        });

        workModeButton.addEventListener("click", function() {
            window.location.href = "/work_mode";
        });

        multiModeButton.addEventListener("click", function(){
            window.location.href = "/multi_mode";
        });

    </script>
   </body>
   ```
2. Test Mode界面：提供基础测试的输入接口与展示窗口
   ```javascript
   <body>
    <h1>Encryption and Decryption</h1>
    
    <div class="form-container">
        <div class="form-row">
            <label for="type">Select form:</label>
            <select title="Select the input information form:" name="form" id="form-select">
                <option value="Binary" selected>Binary</option>
                <option value="Hex">Hex</option>
                <option value="ASCII">ASCII</option>
            </select>
        </div>
        <div class="form-row">
            <label for="message">Message:</label>
            <input type="text" id="message" placeholder="Enter your message">
        </div>
        <div class="form-row">
            <label for="key">Key:</label>
            <input type="text" id="key" placeholder="Enter your key">
        </div>
    </div>

    <div class="buttons-container">
        <button id="Encrypt" onclick="encryptMessage()">Encrypt</button>
        <button id="Decrypt" onclick="decryptMessage()">Decrypt</button>
    </div>

    <div id="iframeContainer">
        <iframe title="iframe-title" id="iframe" src="about:blank"></iframe>
    </div>
    <br/>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <script>
        function sendRequest(form,message,key,action) {
            $.ajax({
                type:"POST",
                url:"/test_mode/"+action,
                timeout:5000,
                contentType: "application/json",
                data: JSON.stringify({              // 将数据转换为JSON字符串
                    form: form,
                    message: message,
                    key:key
                }),
                success:function(responseData){
                    console.log(responseData);
                    if (action == 'encryptMessage'){
                        var my_iframe = document.getElementById('iframe');
                        my_iframe.contentDocument.body.innerHTML = "";
                        if (form == 'ASCII'){
                            var encodedString = responseData;
                            var parser = new DOMParser();
                            var decodedDocument = parser.parseFromString('<!doctype html><body>' + encodedString, 'text/html');
                            var responseData = decodedDocument.body.textContent;
                        }
                        my_iframe.contentDocument.body.innerHTML = "CipherText: " + responseData;
                    }
                    else if (action == 'decryptMessage'){
                        var my_iframe = document.getElementById('iframe');
                        my_iframe.contentDocument.body.innerHTML = "";
                        if (form == 'ASCII'){
                            var encodedString = responseData;
                            var parser = new DOMParser();
                            var decodedDocument = parser.parseFromString('<!doctype html><body>' + encodedString, 'text/html');
                            var responseData = decodedDocument.body.textContent;
                        }
                        my_iframe.contentDocument.body.innerHTML = "PlainText: " + responseData;
                    }
                },
                error: function(xhr, status, error) {
                    console.log("Error: " + error);
                }
            });
        }

        function encryptMessage() {
            event.preventDefault();
            var form = document.getElementById('form-select').value;
            var message = document.getElementById("message").value;
            var key = document.getElementById("key").value;
            if (form === 'Binary' && !isValidBinaryMessage(message)) {
                alert("The len of message(Binary) must be a multiple of 16! Please retype");
                return;
            }

            if (form === 'Hex' && !isValidHexMessage(message)){
                alert("The len of message(Hex) must be a multiple of 4! Please retype");
                return;
            }
            if (form ==='ASCII' && !isValidAsciiMessage(message)){
                alert("The len of message(Ascii) must be a multiple of 2! Please retype")
            }
            if ((form === 'Binary' || form === 'ASCII') && !isValidKey_binary(key)) {
                alert("Key must be Binary(16-bit)! Please retype");
                return;
            }

            if (form === 'Hex' && !isValidKey_hex(key)){
                alert("Key must be Hex(4)! Please retype");
                return;
            }
            sendRequest(form, message, key, 'encryptMessage');
        }

        function decryptMessage() {
            event.preventDefault();
            var form = document.getElementById('form-select').value;
            var message = document.getElementById("message").value;
            var key = document.getElementById("key").value;

            if (form === 'Binary' && !isValidBinaryMessage(message)) {
                alert("The len of message(Binary) must be a multiple of 16! Please retype");
                return;
            }

            if (form === 'Hex' && !isValidHexMessage(message)){
                alert("The len of message(Hex) must be a multiple of 4! Please retype");
                return;
            }
            if (form==='ASCII' && !isValidAsciiMessage(message)){
                alert("The len of message(Ascii) must be a multiple of 2! Please retype")
            }
            if ((form === 'Binary' || form === 'ASCII') && !isValidKey_binary(key)) {
                alert("Key must be Binary(16-bit)! Please retype");
                return;
            }

            if (form === 'Hex' && !isValidKey_hex(key)){
                alert("Key must be Hex(4)! Please retype");
                return;
            }
            sendRequest(form, message, key, 'decryptMessage');
        }

        // message如果是二进制字符串,长度只能是16-bit的整数倍
        function isValidBinaryMessage(message) {
            if (message.length % 16 !== 0 || !/^[01]+$/.test(message)) {
                return false;
            }
            return true;
        }

        function isValidHexMessage(message){
            if (message.length %4 !== 0 || !/^[0-9A-Fa-f]+$/.test(message)){
                return false;
            }
            return true;
        }
        function isValidAsciiMessage(message){
            if (message.length % 2 !==0){
                return false;
            }
            return true;
        }
        // key只能是Binary(16-bit)字符串
        function isValidKey_binary(key){
            if (key.length !== 16 || !/^[01]+$/.test(key)) {
                return false;
            }
            return true;
        }
        //key只能是Hex(4)字符串 addition
        function isValidKey_hex(key){
            var hexPattern = /^[0-9A-Fa-f]{4}$/;
            if (hexPattern.test(key)) {
                return true; 
            } else {
                return false; 
            }
        }

        $(document).ready(function() {
            $("#form-select, #message, #key").change(function() {
                // 重置iframe内容
                var my_iframe = document.getElementById("iframe");
                my_iframe.srcdoc = "";
                });

            $("#Encrypt").click(function() {
                encryptMessage();
            });

            $("#Decrypt").click(function() {
                decryptMessage();
            });
        });
    </script>
   </body>
   ```
3. Work Mode界面：模拟实际使用，支持加密任意长度的二进制明文
   ```javascript
   <body>
    <h1>CBC Work Mode</h1>

    <div class="container">
        <label for="inputText">InputText:</label>
        <input type="text" id="inputText" name="inputText" placeholder="Binary string">
    </div>

    <div class="container">
        <label for="padding">Padding:</label>
        <input type="text" id="padding" name="padding" placeholder="For decryption: default 0">
        </div>
    </div>

    <div class="container">
        <label for="inputKey">InputKey:</label>
        <input type="text" id="inputKey" name="inputKey" placeholder="16-bit Binary mother key">
    </div>

    <div class="action-buttons">
        <button id="encryptionButton" onclick="encryptText()">Encryption</button>
        <button id="decryptionButton" onclick="decryptText()">Decryption</button>
    </div>


    <div id="iframeContainer">
        <iframe title="iframe-title" id="iframe" src="about:blank"></iframe>
    </div>

    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>
        function sendRequest(inputText, inputKey, padding, action){
            $.ajax({
                type:"POST",
                url:"/work_mode/"+action,
                timeout:5000,
                contentType: "application/json",
                data: JSON.stringify({              
                    inputText: inputText,
                    inputKey: inputKey,
                    padding: padding,
                }),
                success:function(responseData){
                    //console.log(responseData);
                    if (action=='encryptText'){
                        var responseData = JSON.parse(responseData);
                        var result = responseData.result;
                        var padding = responseData.padding;
                        var my_iframe = document.getElementById('iframe');
                        my_iframe.contentDocument.body.innerHTML = "";
                        my_iframe.contentDocument.body.innerHTML = "Ciphertext:\n" + result + "\n\nPadding:\n " + padding;
                    }
                    else if (action=='decryptText'){
                        console.log(responseData);
                        var my_iframe = document.getElementById('iframe');
                        my_iframe.contentDocument.body.innerHTML = "";
                        my_iframe.contentDocument.body.innerHTML = "Plaintext: " + responseData;
                    }
                }, 
                error: function(xhr, status, error) {
                    console.log("Error: " + error);
                }
            });
        }

        function encryptText() {
            event.preventDefault();
            var inputText = document.getElementById('inputText').value;
            var inputKey = document.getElementById("inputKey").value;
            var padding = 0;

            if (!isValidBinaryInputText_en(inputText)) {
                alert("The inputText must be Binary! Please retype");
                return;
            }

            if (!isValidKey(inputKey)) {
                alert("Key must be binary(16-bit)! Please retype");
                return;
            }
            sendRequest(inputText, inputKey, padding, 'encryptText');
        }

        
        function decryptText(){
            event.preventDefault();
            var inputText = document.getElementById('inputText').value;
            var inputKey = document.getElementById("inputKey").value;
            var padding = document.getElementById("padding").value;

            if (!isValidBinaryInputText_de(inputText)) {
                alert("The inputText must be binary and a multiple of 16! Please retype");
                return;
            }

            if (!validatePaddingInput(padding, inputText)){
                alert("Padding must be a non-negative integer.");
                return;
            }

            if (padding === ""){
                var padding = parseInt('0',10);
            }
            else{
                var padding = parseInt(padding, 10);
            }

            if (!isValidKey(inputKey)) {
                alert("Key must be binary(16-bit)! Please retype");
                return;
            }
            console.log(inputText)
            console.log(padding)
            console.log(inputKey)
            sendRequest(inputText, inputKey, padding, 'decryptText');
        }

        //加密时对输入内容的要求: 二进制字符串
        function isValidBinaryInputText_en(inputText){
            if (!/^[01]+$/.test(inputText)){
                return false;
            }
            return true
        }
        //解密时对输入内容的要求：二进制字符串,长度是16的整数
        function isValidBinaryInputText_de(inputText){
            if (inputText.length % 16 !== 0 || !/^[01]+$/.test(inputText)){
                return false;
            }
            return true
        }
        //对密钥的要求: 16bits二进制字符串
        function isValidKey(key){
            if (key.length !== 16 || !/^[01]+$/.test(key)) {
                return false;
            }
            return true;
        }
        //对填充值的要求: 0或正整数
        function validatePaddingInput(padding, inputText) {
            if (padding === "") {
                return true; 
            }
            else if (/^[0-9]+$/.test(padding) && parseInt(padding, 10) >= 0 && parseInt(padding, 10) < inputText.length) {
                return true;
            } 
            else { 
                return false;
            }
        }


        $(document).ready(function() {
            $("#inputText, #inputKey, #padding").change(function() {
                // 重置iframe内容
                var my_iframe = document.getElementById("iframe");
                my_iframe.srcdoc = "";
                });

            $("#encryptionButton").click(function() {
                encryptText();
            });

            $("#decryptionButton").click(function() {
                decryptText();
            });

        });

    </script>
   </body>
   ```
4. Multi Mode: 提供双重加解密和三重加解密的用户接口
   ```javascript
   <body>
    <h1>Multiple Encryption and Decryption</h1>
    
    <div class="form-container">
        <div class="form-row">
            <label for="type">Select form:</label>
            <select title="Select the en-decryption method:" name="form" id="form-select">
                <option value="double" selected>Double en-decryption</option>
                <option value="three">Three en-decryption</option>
            </select>
        </div>

        <div class="form-row">
            <label for="message">Message:</label>
            <input type="text" id="message" placeholder="Enter your message">
        </div>

        <div class="form-row">
            <label for="key">Key:</label>
            <input type="text" id="key" placeholder="Enter your key">
        </div>
    </div>

    <div class="buttons-container">
        <button id="Encrypt" onclick="encryptMessage()">Encrypt</button>
        <button id="Decrypt" onclick="decryptMessage()">Decrypt</button>
    </div>

    <div id="iframeContainer">
        <iframe title="iframe-title" id="iframe" src="about:blank"></iframe>
    </div>
    <br/>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <script>
        function sendRequest(form,message,key,action) {
            $.ajax({
                type:"POST",
                url:"/multi_mode/"+action,
                timeout:5000,
                contentType: "application/json",
                data: JSON.stringify({              
                    form: form,
                    message: message,
                    key:key
                }),
                success:function(responseData){
                    console.log(responseData);
                    if (action == 'encryptMessage'){
                        var my_iframe = document.getElementById('iframe');
                        my_iframe.contentDocument.body.innerHTML = "";
                        my_iframe.contentDocument.body.innerHTML = "CipherText: " + responseData;
                    }
                    else if (action == 'decryptMessage'){
                        var my_iframe = document.getElementById('iframe');
                        my_iframe.contentDocument.body.innerHTML = "";
                        my_iframe.contentDocument.body.innerHTML = "PlainText: " + responseData;
                    }
                },
                error: function(xhr, status, error) {
                    console.log("Error: " + error);
                }
            });
        }

        function encryptMessage() {
            event.preventDefault();
            var form = document.getElementById('form-select').value;
            var message = document.getElementById("message").value;
            var key = document.getElementById("key").value;
            if (!isValidBinaryMessage(message)) {
                alert("The len of message(Binary) must be 16!\nPlease retype");
                return;
            }

            if (!isValidKey(form, key)) {
                alert("If double de-encryption, then len(key) = 32; \nIf three en-decryption, then len(key) = 48!\nPlease retype");
                return;
            }
            sendRequest(form, message, key, 'encryptMessage');
        }

        function decryptMessage() {
            event.preventDefault();
            var form = document.getElementById('form-select').value;
            var message = document.getElementById("message").value;
            var key = document.getElementById("key").value;

            if (!isValidBinaryMessage(message)) {
                alert("The len of message(Binary) must be 16!\nPlease retype");
                return;
            }

            if (!isValidKey(form, key)) {
                alert("If double de-encryption, then len(key) = 32; \nIf three en-decryption, then len(key) = 48!\nPlease retype");
                return;
            }
            sendRequest(form, message, key, 'decryptMessage');
        }

        // message只能是16bits的二进制字符串
        function isValidBinaryMessage(message) {
            if (message.length  !== 16 || !/^[01]+$/.test(message)) {
                return false;
            }
            return true;
        }
        
        function isValidKey(form, key){
            if (form === 'double'){
                if ((key.length !== 32 || !/^[01]+$/.test(key))) {
                    return false;
                }
            }
            else if (form === 'three'){
                if ((key.length !== 48 || !/^[01]+$/.test(key))) {
                    return false;
                }
            }
            return true;
        }

        $(document).ready(function() {
            $("#form-select, #message, #key").change(function() {
                var my_iframe = document.getElementById("iframe");
                my_iframe.srcdoc = "";
                });

            $("#Encrypt").click(function() {
                encryptMessage;
            });

            $("#Decrypt").click(function() {
                decryptMessage;
            });
        });
    </script>
   </body>
   ```

5. 前后端交互设置：各个界面的功能路由都是界面路由的子路由
   ```python
   @app.route('/', methods=['GET', 'POST'])
   def home():
       return render_template('home.html')
   
   @app.route('/work_mode', methods=['GET'])
   def work_mode():
       return render_template('work_mode.html')
   
   @app.route('/work_mode/encryptText', methods=['GET','POST'])
   def work_encrypt():
       if request.method == 'POST':
           data = request.get_json()
           inputText = data['inputText']
           inputKey = data['inputKey']
           padding = data['padding']
           seed = 12345
           result, padding = CBC.CBC_encryption(inputText, inputKey, seed, padding)
           response_data = {
               'result': result,
               'padding': padding
           }
           json_response = json.dumps(response_data)
           return json_response
       else:
           return 'Invalid request method'
       
   @app.route('/work_mode/decryptText', methods=['GET','POST'])
   def work_decrypt():
       if request.method == 'POST':
           data = request.get_json()
           inputText = data['inputText']
           inputKey = data['inputKey']
           padding = data['padding']
           seed = 12345
           result = CBC.CBC_decryption(inputText, inputKey, seed, padding)
           return result
       else:
           return 'Invalid request method'
   
   @app.route('/test_mode', methods=['GET'])
   def test_mode():
       return render_template('test_mode.html')
   
   @app.route('/test_mode/encryptMessage', methods=['GET', 'POST'])
   def encrypt():
       if request.method == 'POST':
           data = request.get_json()
           form = data['form']
           message = data['message']
           key = data['key']
           if form == 'Binary':      
               res = encrypting.encrypting_binaryStr(message, key)
           elif form == 'ASCII':
               res = encrypting.encrypting_ascii(message, key)
           else:
               res = encrypting.encrypting_hexadecimal(message, key)
           return res
       else:
           return "Invalid request method."
       
   @app.route('/test_mode/decryptMessage', methods=['GET', 'POST'])
   def decrypt():
       if request.method == 'POST':
           data = request.get_json()
           form = data['form']
           message = data['message']
           key = data['key']
           if form == 'Binary':      
               res = decrypting.decrypting_binaryStr(message, key)
           elif form == 'ASCII':
               res = decrypting.decrypting_ascii(message, key)
           else:
               res = decrypting.decrypting_hexadecimal(message, key)
           return res
       else:
           return "Invalid request method."
   
   
   
   @app.route('/multi_mode', methods=['GET'])
   def multi_mode():
       return render_template('multi_mode.html')
   
   @app.route('/multi_mode/encryptMessage', methods=['GET', 'POST'])
   def multi_encrypt():
       if request.method == 'POST':
           data = request.get_json()
           form = data['form']
           message = data['message']
           key = data['key']
           if form == 'double':      
               res = encrypting.encrypting_double(message, key)
           else:
               res = encrypting.encrypting_three(message, key)
           return res
       else:
           return "Invalid request method."
       
   @app.route('/multi_mode/decryptMessage', methods=['GET', 'POST'])
   def multi_decrypt():
       if request.method == 'POST':
           data = request.get_json()
           form = data['form']
           message = data['message']
           key = data['key']
           if form == 'double':      
               res = decrypting.decrypting_double(message, key)
           else:
               res = decrypting.decrypting_three(message, key)
           return res
       else:
           return "Invalid request method."
   ```
