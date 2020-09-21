#!/usr/bin/env python3

xored = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
x= []
flag=""
key = "jowls" #"ctflearn{"
i=0
for i in xored:
    x.append(ord(i))

for i in range(len(x)):
    flag += chr(x[i] ^ ord(key[i % len(key)]))
    i+=1
print(flag)

