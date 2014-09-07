#!/usr/bin/env python
# coding=utf8
# Flower Password Python Version.
# Author: xLsDg (xlsdg.github.com)
# Origin: http://www.flowerpassword.com/
# Usage: flowerPassword3.py KEY

import sys
import hmac

def calcFlowerPassword(password, key):
    """计算花密"""
    md5one = hmac.new(key.encode(encoding="utf-8"), password.encode(encoding="utf-8")).hexdigest()
    md5two = hmac.new("snow".encode(encoding="utf-8"), md5one.encode(encoding="utf-8")).hexdigest()
    md5three = hmac.new("kise".encode(encoding="utf-8"), md5one.encode(encoding="utf-8")).hexdigest()

    rule = list(md5three)
    source = list(md5two)
    for i in range(0, 32):
        if rule[i].isalpha():
            if rule[i] in "sunlovesnow1990090127xykab":
                source[i] = source[i].upper()

    if source[0].isalpha():
        code16 = "".join(source[0:16])
    else:
        code16 = "K" + "".join(source[1:16])
    #code32 = ''.join(source)
    return code16

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage = "Usage: %s KEY\n" % (sys.argv[0])
        sys.stderr.write(usage)
        sys.exit(1)
    else:
        print calcFlowerPassword("password", sys.argv[1])

