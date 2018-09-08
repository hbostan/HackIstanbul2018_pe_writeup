#!/usr/bin/python3

import hashlib
import itertools

first = "k"
alphabeth = ['h','a','c','i','s','t','a','n','b','u','l']
len_flag = len('k***********')
crack = "29f25103ac08b6452697019e2cc2176e"
cur_hash = ""
val = ""
for cur_hash in itertools.permutations(alphabeth, 11):
  cur_hash = 'k'+''.join(cur_hash)
  val = str(hashlib.md5(cur_hash.encode()).hexdigest())
  if(val == crack):
    print(cur_hash + " : " + val + "   " + crack)
    break

