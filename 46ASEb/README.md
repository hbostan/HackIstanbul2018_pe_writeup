# 46ESAb

  We are given a base64 encoded string, and we are told that there is some custom encryption (obviously apart from base64 encoding). The hint says "it's all in the name".      
  So what's up with the challange name? We can see that it is "Base64" with cases of the letters swapped and the whole string reversed.      
  Let's try few things, 
    - Directly Base64 decode the ciphertext
    - Reverse and case invert the ciphertext then B64 decode
    - B64 decode ciphertext, then case invert and reverse the result, and then B64 decode again.

Luckly the last thing we tried is the correct one.

``` Magic mirror, on the wall, who is the flagest one of all: 51lv3rl1n1n65```
