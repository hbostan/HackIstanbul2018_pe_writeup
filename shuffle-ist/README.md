# shuffle-ist

We are given an md5 hash and some more info to help us crack it.
  - Our alphabeth only consists of `hackistanbul`'s letters. 
  - Our flag starts with `k` and exactly `12` letters long

Let's write a script to crack the hash and get our flag. In the script we create all permutations of `hackistanbul` which start with `k` and compute their hashes to see if they match with the given hash.

```
$ ./pwn.py 
kbahlinsutac : 29f25103ac08b6452697019e2cc2176e   29f25103ac08b6452697019e2cc2176e
```

Our flag is `kbahlinsutac`
