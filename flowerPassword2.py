#!/usr/bin/env python
# coding=utf8
# Flower Password Python Version.
# Author: xLsDg (xlsdg.github.com)
# Origin: http://www.flowerpassword.com/
# Usage: flowerPassword2.py KEY

import sys
import hmac

def generateFPCode(password, key, length = 16):
    if (1 > len(password.strip())) or (1 > len(key.strip())) or (1 > length) or (length > 32):
        return;

    hmd5 = hmac.new(key, password).hexdigest();
    rule = list(hmac.new("kise", hmd5).hexdigest());
    source = list(hmac.new("snow", hmd5).hexdigest());

    for i in range(0, 32):
        if not(source[i].isdigit()):
            if rule[i] in "sunlovesnow1990090127xykab":
                source[i] = source[i].upper();

    code = "".join(source[1:length]);
    if not(source[0].isdigit()):
        code = source[0] + code;
    else:
        code = "K" + code;

    return code;

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage = "Usage: %s KEY\n" % (sys.argv[0]);
        sys.stderr.write(usage);
        sys.exit(1);
    else:
        print generateFPCode("password", sys.argv[1], 16);

