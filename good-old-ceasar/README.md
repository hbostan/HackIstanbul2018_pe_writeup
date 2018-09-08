# good-old-caesar

This is a basic rot cipher challange. But this time our alphabeth is not only letters, it also includes digits. (`[a-z0-9]`). Below is the script's output, we can see that rotating 20 times gives us the flag.

```
$ ./pwn.py 
----------- 0 -----------
4x 34 e4a tyt y9 qwqy3! q17ywx9 t43'9 cqy9 944 2asx za89 9q0u 9xu v1qw q3t 574suut 94 9xu 3ud9 43u. xu7u y8 e4a7 v1qw: lxhvnh3g7tj7l
----------- 1 -----------
5y 45 f5b uzu za rxrz4! r28zxya u54'a drza a55 3bty 0b9a ar1v ayv w2rx r4u 685tvvu a5 ayv 4vea 54v. yv8v z9 f5b8 w2rx: myiwoi4h8uk8m
----------- 2 -----------
6z 56 g6c v0v 0b sys05! s390yzb v65'b es0b b66 4cuz 1cab bs2w bzw x3sy s5v 796uwwv b6 bzw 5wfb 65w. zw9w 0a g6c9 x3sy: nzjxpj5i9vl9n
----------- 3 -----------
70 67 h7d w1w 1c tzt16! t4a1z0c w76'c ft1c c77 5dv0 2dbc ct3x c0x y4tz t6w 8a7vxxw c7 c0x 6xgc 76x. 0xax 1b h7da y4tz: o0kyqk6jawmao
----------- 4 -----------
81 78 i8e x2x 2d u0u27! u5b201d x87'd gu2d d88 6ew1 3ecd du4y d1y z5u0 u7x 9b8wyyx d8 d1y 7yhd 87y. 1yby 2c i8eb z5u0: p1lzrl7kbxnbp
----------- 5 -----------
92 89 j9f y3y 3e v1v38! v6c312e y98'e hv3e e99 7fx2 4fde ev5z e2z 06v1 v8y ac9xzzy e9 e2z 8zie 98z. 2zcz 3d j9fc 06v1: q2m0sm8lcyocq
----------- 6 -----------
a3 9a kag z4z 4f w2w49! w7d423f za9'f iw4f faa 8gy3 5gef fw60 f30 17w2 w9z bday00z fa f30 90jf a90. 30d0 4e kagd 17w2: r3n1tn9mdzpdr
----------- 7 -----------
b4 ab lbh 050 5g x3x5a! x8e534g 0ba'g jx5g gbb 9hz4 6hfg gx71 g41 28x3 xa0 cebz110 gb g41 a1kg ba1. 41e1 5f lbhe 28x3: s4o2uoane0qes
----------- 8 -----------
c5 bc mci 161 6h y4y6b! y9f645h 1cb'h ky6h hcc ai05 7igh hy82 h52 39y4 yb1 dfc0221 hc h52 b2lh cb2. 52f2 6g mcif 39y4: t5p3vpbof1rft
----------- 9 -----------
d6 cd ndj 272 7i z5z7c! zag756i 2dc'i lz7i idd bj16 8jhi iz93 i63 4az5 zc2 egd1332 id i63 c3mi dc3. 63g3 7h ndjg 4az5: u6q4wqcpg2sgu
----------- 10 -----------
e7 de oek 383 8j 0608d! 0bh867j 3ed'j m08j jee ck27 9kij j0a4 j74 5b06 0d3 fhe2443 je j74 d4nj ed4. 74h4 8i oekh 5b06: v7r5xrdqh3thv
----------- 11 -----------
f8 ef pfl 494 9k 1719e! 1ci978k 4fe'k n19k kff dl38 aljk k1b5 k85 6c17 1e4 gif3554 kf k85 e5ok fe5. 85i5 9j pfli 6c17: w8s6yseri4uiw
----------- 12 -----------
g9 fg qgm 5a5 al 282af! 2dja89l 5gf'l o2al lgg em49 bmkl l2c6 l96 7d28 2f5 hjg4665 lg l96 f6pl gf6. 96j6 ak qgmj 7d28: x9t7ztfsj5vjx
----------- 13 -----------
ha gh rhn 6b6 bm 393bg! 3ekb9am 6hg'm p3bm mhh fn5a cnlm m3d7 ma7 8e39 3g6 ikh5776 mh ma7 g7qm hg7. a7k7 bl rhnk 8e39: yau80ugtk6wky
----------- 14 -----------
ib hi sio 7c7 cn 4a4ch! 4flcabn 7ih'n q4cn nii go6b domn n4e8 nb8 9f4a 4h7 jli6887 ni nb8 h8rn ih8. b8l8 cm siol 9f4a: zbv91vhul7xlz
----------- 15 -----------
jc ij tjp 8d8 do 5b5di! 5gmdbco 8ji'o r5do ojj hp7c epno o5f9 oc9 ag5b 5i8 kmj7998 oj oc9 i9so ji9. c9m9 dn tjpm ag5b: 0cwa2wivm8ym0
----------- 16 -----------
kd jk ukq 9e9 ep 6c6ej! 6hnecdp 9kj'p s6ep pkk iq8d fqop p6ga pda bh6c 6j9 lnk8aa9 pk pda jatp kja. dana eo ukqn bh6c: 1dxb3xjwn9zn1
----------- 17 -----------
le kl vlr afa fq 7d7fk! 7iofdeq alk'q t7fq qll jr9e grpq q7hb qeb ci7d 7ka mol9bba ql qeb kbuq lkb. ebob fp vlro ci7d: 2eyc4ykxoa0o2
----------- 18 -----------
mf lm wms bgb gr 8e8gl! 8jpgefr bml'r u8gr rmm ksaf hsqr r8ic rfc dj8e 8lb npmaccb rm rfc lcvr mlc. fcpc gq wmsp dj8e: 3fzd5zlypb1p3
----------- 19 -----------
ng mn xnt chc hs 9f9hm! 9kqhfgs cnm's v9hs snn ltbg itrs s9jd sgd ek9f 9mc oqnbddc sn sgd mdws nmd. gdqd hr xntq ek9f: 4g0e60mzqc2q4
----------- 20 -----------
oh no you did it again! alright don't wait too much just take the flag and proceed to the next one. here is your flag: 5h1f71n0rd3r5
----------- 21 -----------
pi op zpv eje ju bhbjo! bmsjhiu epo'u xbju upp nvdi kvtu ublf uif gmbh boe qspdffe up uif ofyu pof. ifsf jt zpvs gmbh: 6i2g82o1se4s6
----------- 22 -----------
qj pq 0qw fkf kv cickp! cntkijv fqp'v yckv vqq owej lwuv vcmg vjg hnci cpf rtqeggf vq vjg pgzv qpg. jgtg ku 0qwt hnci: 7j3h93p2tf5t7
----------- 23 -----------
rk qr 1rx glg lw djdlq! douljkw grq'w zdlw wrr pxfk mxvw wdnh wkh iodj dqg surfhhg wr wkh qh0w rqh. khuh lv 1rxu iodj: 8k4ia4q3ug6u8
----------- 24 -----------
sl rs 2sy hmh mx ekemr! epvmklx hsr'x 0emx xss qygl nywx xeoi xli jpek erh tvsgiih xs xli ri1x sri. livi mw 2syv jpek: 9l5jb5r4vh7v9
----------- 25 -----------
tm st 3tz ini ny flfns! fqwnlmy its'y 1fny ytt rzhm ozxy yfpj ymj kqfl fsi uwthjji yt ymj sj2y tsj. mjwj nx 3tzw kqfl: am6kc6s5wi8wa
----------- 26 -----------
un tu 4u0 joj oz gmgot! grxomnz jut'z 2goz zuu s0in p0yz zgqk znk lrgm gtj vxuikkj zu znk tk3z utk. nkxk oy 4u0x lrgm: bn7ld7t6xj9xb
----------- 27 -----------
vo uv 5v1 kpk p0 hnhpu! hsypno0 kvu'0 3hp0 0vv t1jo q1z0 0hrl 0ol mshn huk wyvjllk 0v 0ol ul40 vul. olyl pz 5v1y mshn: co8me8u7ykayc
----------- 28 -----------
wp vw 6w2 lql q1 ioiqv! itzqop1 lwv'1 4iq1 1ww u2kp r201 1ism 1pm ntio ivl xzwkmml 1w 1pm vm51 wvm. pmzm q0 6w2z ntio: dp9nf9v8zlbzd
----------- 29 -----------
xq wx 7x3 mrm r2 jpjrw! ju0rpq2 mxw'2 5jr2 2xx v3lq s312 2jtn 2qn oujp jwm y0xlnnm 2x 2qn wn62 xwn. qn0n r1 7x30 oujp: eqaogaw90mc0e
----------- 30 -----------
yr xy 8y4 nsn s3 kqksx! kv1sqr3 nyx'3 6ks3 3yy w4mr t423 3kuo 3ro pvkq kxn z1ymoon 3y 3ro xo73 yxo. ro1o s2 8y41 pvkq: frbphbxa1nd1f
----------- 31 -----------
zs yz 9z5 oto t4 lrlty! lw2trs4 ozy'4 7lt4 4zz x5ns u534 4lvp 4sp qwlr lyo 02znppo 4z 4sp yp84 zyp. sp2p t3 9z52 qwlr: gscqicyb2oe2g
----------- 32 -----------
0t z0 a06 pup u5 msmuz! mx3ust5 p0z'5 8mu5 500 y6ot v645 5mwq 5tq rxms mzp 130oqqp 50 5tq zq95 0zq. tq3q u4 a063 rxms: htdrjdzc3pf3h
----------- 33 -----------
1u 01 b17 qvq v6 ntnv0! ny4vtu6 q10'6 9nv6 611 z7pu w756 6nxr 6ur synt n0q 241prrq 61 6ur 0ra6 10r. ur4r v5 b174 synt: iueske0d4qg4i
----------- 34 -----------
2v 12 c28 rwr w7 ouow1! oz5wuv7 r21'7 aow7 722 08qv x867 7oys 7vs tzou o1r 352qssr 72 7vs 1sb7 21s. vs5s w6 c285 tzou: jvftlf1e5rh5j
----------- 35 -----------
3w 23 d39 sxs x8 pvpx2! p06xvw8 s32'8 bpx8 833 19rw y978 8pzt 8wt u0pv p2s 463rtts 83 8wt 2tc8 32t. wt6t x7 d396 u0pv: kwgumg2f6si6k
```

