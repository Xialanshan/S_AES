S = [[0x9, 0x4, 0xA, 0xB],
    [0xD, 0x1, 0x8, 0x5],
    [0x6, 0x2, 0x0, 0x3],
    [0xC, 0xE, 0xF, 0x7]]     


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


