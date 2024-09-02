# Asal Nama Sabah
> Setiap negeri mempunyai asal nama negeri tersebut. Begitu juga dengan negeri Sabah. Sabah juga mempunyai nama asal negeri tersebut yang popular di kalangan masyarakat tempatan.

![](https://i.imgur.com/Aw97YoB.png)

Flag: 3108{S4B4H_S4PP4H}

#ctf #rev

---
We are given an executable file for this challenge. I go ahead and throw the file to [DogBolt](https://dogbolt.org/?id=07d3a82f-ca8a-4e27-bd49-f3956982db49)(great platform to test various decompilers). After decompiling, I chose the Hex-Rays decompiler as it seems to be more readable.

The function that we should put our focus on is this *check_flag* function.

![](https://i.imgur.com/mAS3f5W.png)

Basically the each character from `s2` will be XORed with each character from `s`. With that I used ChatGPT to help me craft the script to decode the flag.
##### Solution.py
```python
s = "namaasalsabah"
s2 = "5d505d591a20552e47293d325c3e3159291c"
v4 = len(s) #13

# Convert hex string to a list of integers
s2_bytes = [int(s2[i:i+2], 16) for i in range(0, len(s2), 2)]

# XOR with corresponding characters from s
decoded_bytes = [s2_bytes[i] ^ ord(s[i % v4]) for i in range(len(s2_bytes))]

# Convert decoded bytes back to a string
decoded_string = ''.join(chr(b) for b in decoded_bytes)
print("Decoded flag:", decoded_string)
```

![](https://i.imgur.com/YNeEixF.png)