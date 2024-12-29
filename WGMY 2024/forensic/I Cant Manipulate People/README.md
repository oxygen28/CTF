# I Cant Manipulate People
> Partial traffic packet captured from hacked machine, can you analyze the provided pcap file to extract the message from the packet perhaps by reading the packet data?
> 
> Hint: Attacker too noob to ping not in sequence

![](https://i.imgur.com/YDFlqCz.png)

Flag: WGMY{1e3b71d57e466ab71b43c2641a4b34f4}

#ctf #forensic #pcap #wireshark 

---
Given a `traffic.pcap` file, it can be observed in Wireshark that the source is sending a large number of ping requests to `192.168.0.1` with the following information: `Echo (ping) request id=0x0000, seq=0/0, ttl=64 (no response found!)`. By examining the packet, we see that the data section of each packet consists of only 1 byte.

To filter and view only ICMP Echo requests, apply the filter `icmp.type == 8`. Then, modify the protocol preferences by right-clicking on any packet and selecting `Protocol Preferences > Data > Show Data as Text`. This will display the entire data section of the ping packet, where the flag is visible.

![](https://i.imgur.com/VvWTsqf.png)

An alternative way to obtain the flag is by using Tshark. The following command can be run in the terminal:

```bash
tshark -r traffic.pcap -Y "icmp.type == 8" -T fields -e data | xxd -r -p
```

![](https://i.imgur.com/9wfl2Na.png)
