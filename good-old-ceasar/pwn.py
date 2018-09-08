#!/usr/bin/python3

import string

cipher = "4x 34 e4a tyt y9 qwqy3! q17ywx9 t43'9 cqy9 944 2asx za89 9q0u 9xu v1qw q3t 574suut 94 9xu 3ud9 43u. xu7u y8 e4a7 v1qw: lxhvnh3g7tj7l"

letters = string.ascii_lowercase+string.digits
letters_length = len(letters)
for i in range(letters_length):
  print("-----------", i , "-----------")
  res = ""
  for lt in cipher:
      idx = letters.find(lt)
      if idx != -1:
          idx = (idx + i) % letters_length
          res += letters[idx]
      else:
          res += lt
  print(res)
