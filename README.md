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
#### 1.固定参数

S盒：<img width="168" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/18a16da9-d723-424d-aef1-d7bd22530090">

逆S盒：<img width="181" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/9d52291d-e106-4b29-83ea-c0045cea4716">

列混淆矩阵：<img width="101" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/c9de8aa3-95bf-469f-92b9-bb139a050c64">

逆列混淆矩阵：<img width="128" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/18425bf6-994a-41d5-bd20-1c0b8025270d">

#### 2.密钥拓展
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
