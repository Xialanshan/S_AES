import utils


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

