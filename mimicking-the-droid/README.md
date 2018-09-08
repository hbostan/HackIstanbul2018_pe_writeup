# mimicking-the-droid     
     
In this challange we need to generate the `gesture.key` file that android devices use to unlock the phone. Most of the people I know use the "connect-the-dots" or the grid version (instead of a password). There are 9 dots and the pattern you connect them becomes your password.
Android enumerates the dots as follows:

```
0  1  2
3  4  5
6  7  8
```

And stores them in the gesture.key file by sha1 hashing the pattern. For example if our pattern was `0-1-2-4-5` our gesture.key file would contain `\xe1\x6a\xd6\x4c\x2d\xb1\xd1\x89\x58\x63\x97\x70\x52\x21\x2d\x07\xb8\x70\xca\x45` the sha1 hash of `\x0\x1\x2\x4\x5`.

Now for the challenge.
Our pin needs to be `"8, 4, 0, 2, 1, 5, 3, 7, 6"` so we need to put `\x8\x4\x0\x2\x1\x5\x3\x7\x6` into a file and then calculate the hash.

```
$ echo -ne "\x8\x4\x0\x2\x1\x5\x3\x7\x6" > flag.pin
$ xxd flag.pin 
00000000: 0804 0002 0105 0307 06                   ......... 
$ sha1sum flag.pin | awk '{print $1}' | xxd -r -p > flag.key
$ xxd flag.key 
00000000: 37a1 6dec 5be2 c97b 7bca b65c 96d6 030e  7.m.[..{{..\....
00000010: eb2e e644                                ...D
$ cat flag.key | base64
N6Ft7FviyXt7yrZcltYDDusu5kQ=
```
So our flag is `N6Ft7FviyXt7yrZcltYDDusu5kQ=`.
