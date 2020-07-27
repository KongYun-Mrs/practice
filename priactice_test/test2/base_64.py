# coding: utf-8

import base_64

copyright = 'Copyright (c) 2012 Doucube Inc. All rights reserved.'


def main():
    bytesString = copyright.encode(encoding="utf-8")
    print(bytesString)

    # base64 加密
    encodestr = base_64.b64encode(bytesString)
    print(encodestr)
    # base64 解密
    decodestr = base_64.b64decode(encodestr)
    print(decodestr.decode())


if __name__ == '__main__':
    main()
