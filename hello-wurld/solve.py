#!/usr/bin/python3

with open("hello.txt", "r") as f:
  text = f.read()
  text = text.replace("U+","")
  text = text.split(" ")
  for a in text:
    print(chr(int(a, 16)), end="")
  print()
