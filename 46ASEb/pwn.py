#!/usr/bin/python3

import base64

cipher = 'R3VKblVmSkJYV01DWnloQlh1ZGk2V2dCSGJJelZic3pVOWdpMG54ek5mZ0JNYnN6T3JoaVpMZ2lWSDJER1djQlNmMkRHdWdBMGJJQlZiY2xZOU1DWUx3Qkdtd0FOZnd0Cg=='
cipher_case_inverted = cipher.swapcase()
cipher_reversed = cipher_case_inverted[::-1]+'==' # Added padding eventhough that it doesn't even decode as a string
cipher_reversed_decoded = base64.b64decode(cipher_reversed)
plaintext = base64.b64decode(cipher).decode("utf-8")
plaintext_case_inverted = plaintext.swapcase()
plaintext_reversed = plaintext_case_inverted[::-1]
original_plaintext = base64.b64decode(plaintext_reversed).decode("utf-8")
print("\nCiphertext: \n", cipher)
print("\nCiphertext B64 decoded: \n", plaintext)
print("\nCiphertext reversed, case inverted, B64 decoded: \n", cipher_reversed_decoded)
print("\nCiphertext B64 decoded, case inverted, reversed, and B64 decoded again: \n", original_plaintext)

