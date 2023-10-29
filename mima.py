import copy
import utils
import decrypting


# 第一组加密解密，得到一个列表
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


# 其他组解密
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


"""
明密文对设置
P1 = '0000111100001111'
C1 = '1110010001011110'
P2 = '1111111100000000'
C2 = '0010010001010010'
P3 = '1100110011001101'
C3 = '1010101100100010'

正确密钥
key1 = '0010110101010101'
key2 = '1010011100111011'
"""

def main():
    n=input('已有使用相同明密文对数量：')
    P_list=[]
    C_list=[]
    i=0
    while i<3:
        p=input(f'第{i+1}个明文：')
        c=input(f'第{i+1}个密文：')
        P_list.append(p)
        C_list.append(c)
        i=i+1
    print(meet_in(P_list,C_list))

if __name__ == "__main__":
    main()
