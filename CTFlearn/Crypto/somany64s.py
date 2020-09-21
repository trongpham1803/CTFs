#!/usr/bin/env python3


import base64

with open("flag.txt") as f:
    ctext=f.read()
    for i in range(100):
        ctext = base64.b64decode(ctext)
        if(b'CTF{' in ctext or b'flag{' in ctext):
            print(ctext)
            break
