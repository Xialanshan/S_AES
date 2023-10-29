import GetKeys 

S = [[0x9, 0x4, 0xA, 0xB],
     [0xD, 0x1, 0x8, 0x5],
     [0x6, 0x2, 0x0, 0x3],
     [0xC, 0xE, 0xF, 0x7]]
M = [[0x1, 0x4],
     [0x4, 0x1]]

S_inv = [[0xA, 0x5, 0x9, 0xB],
         [0x1, 0x7, 0x8, 0xF],
         [0x6, 0x0, 0x2, 0x3],
         [0xC, 0x4, 0xD, 0xE]]
M_inv = [[0x9, 0x2],
         [0x2, 0x9]]


def sbox_substitution(input_text, S):
    """
    :param input_text: 需要替换的4bits二进制
    :param S 使用的替换盒
    :return: 返回替换后的4bits二进制数
    """
    row = int(input_text[0] + input_text[1], 2)
    col = int(input_text[2] + input_text[3], 2)
    return format(S[row][col], '04b')


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

