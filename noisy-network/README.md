# noisy-network

We are given a packet capture file. There is a lot of network traffic on the packet capture.
`tshark -r captur.pcap` gives us a lot of unnecessary info.
Let's look at the FTP traffic only 
`$ tshark -r captur.pcap -Y ftp`.
Still a lot of data but we are getting close. We can see some login attempts. Let's filter only the `PASS` commands in ftp requests.
```
$ tshark -r 5b8ff402af82f47.pcap -Y 'ftp.request.command contains "PASS"'
56649  24.409505 172.16.118.150 → 172.16.118.129 FTP 96 Request: PASS isthistheflag_s#210-s89
57026  51.263393 172.16.118.150 → 172.16.118.129 FTP 96 Request: PASS isthistheflag_aJH-xS0g1
57061  79.241963 172.16.118.150 → 172.16.118.129 FTP 96 Request: PASS thisistheflag_O9kLd!!(*
```

Voila! We can see our flag is `thisistheflag_O9kLd!!(*`.
