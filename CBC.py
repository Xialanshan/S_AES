import utils
import GetKeys
import random

def IV_generate(seed):
    random.seed(seed)
    iv = bytes([random.randint(0, 255) for _ in range(2)])
    iv_binary = ''.join(format(byte, '08b') for byte in iv)
    return iv_binary


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


