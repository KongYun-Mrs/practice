# coding: utf-8

from M2Crypto import EVP
from M2Crypto import m2
from M2Crypto import util

ENCRYPT_OP = 1  # 加密操作
DECRYPT_OP = 0  # 解密操作

iv = '\0' * 16  # 初始化变量，对于aes_128_ecb算法无用
PRIVATE_KEY = 'dd7fd4a156d28bade96f816db1d18609'  # 密钥


def Encrypt(data):
    '使用aes_128_ecb算法对数据加密'
    cipher = EVP.Cipher(alg='aes_128_ecb', key=PRIVATE_KEY, iv=iv, op=ENCRYPT_OP)
    buf = cipher.update(data)
    buf = buf + cipher.final()
    del cipher
    # 将明文从字节流转为16进制
    output = ''
    for i in buf:
        output += '%02X' % (ord(i))
    return output


def Decrypt(data):
    '使用aes_128_ecb算法对数据解密'
    # 将密文从16进制转为字节流
    data = util.h2b(data)
    cipher = Cipher(alg='aes_128_ecb', key=PRIVATE_KEY, iv=iv, op=DECRYPT_OP)
    buf = cipher.update(data)
    buf = buf + cipher.final()
    del cipher
    return buf


data = {
    "action": "query",
    "target": {
        "tss_http_client": {
            "method": "$method",
            "uri": "$uri",
            "params": {},
            "data": {},
            "cloud_operator_name": "$cloud_operator_name",
            "cloud_operator_time": 1543487362042,
            "cloud_operator_email": "$cloud_operator_email"
        }
    },
    "args": {
        "timeout": "$timeout",
        "response_async": False
    },
    "msg_type": "request",
    "request_id": "$request_id",
    "created": "$created"
}

ser = Encrypt(data)
print ser

