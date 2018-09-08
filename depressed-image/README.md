# depressed-image

We are given a .jpg image. And the challange title and hints makes me think of there is some hidden data. Let's run `binwalk` to see if there is anything other than an image in our image.

```
$ binwalk -e  image.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
434217        0x6A029         7-zip archive data, version 0.4
```

So there is a 7-zip archive appended to the end of our image. Let's extract it.

```
$ 7z e image.jpg

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,16 CPUs AMD Ryzen 7 1700 Eight-Core Processor           (800F11),ASM,AES-NI)

Scanning the drive for archives:
1 file, 434409 bytes (425 KiB)

Extracting archive: image.jpg
--
Path = image.jpg
Type = 7z
Offset = 434217
Physical Size = 192
Headers Size = 130
Method = LZMA2:12
Solid = -
Blocks = 1

Everything is Ok

Size:       61
Compressed: 434409
$ ls
image.jpg  y0uRfl46.txt
$ cat y0uRfl46.txt 
Same spot same time this time your password is f98d0ks0aBr13
```

Flag is `f98d0ks0aBr13`.

