import utils


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


