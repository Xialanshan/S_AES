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

   | 明文    | 0000111100001111     | 1111111100000000     | 1100110011001101 | 
| ------- | ------- | ------- | ---------|
| 密文   | 1110010001011110   |0010010001010010  | 1010101100100010|

密钥设置：<img width="161" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/ff8e0be2-38c0-41bf-bc0a-c1f0bdaa4667">

<img width="234" alt="image" src="https://github.com/Xialanshan/S_AES/assets/110965468/c8ea304f-b919-4d48-9337-2c1b14381ab7">

返回结果 == key1 + key2

