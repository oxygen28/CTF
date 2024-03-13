# Iced Tea
> Locked within a cabin crafted entirely from ice, you're enveloped in a chilling silence. Your eyes land upon an old notebook, its pages adorned with thousands of cryptic mathematical symbols. Tasked with deciphering these enigmatic glyphs to secure your escape, you set to work, your fingers tracing each intricate curve and line with determination. As you delve deeper into the mysterious symbols, you notice that patterns appear in several pages and a glimmer of hope begins to emerge. Time is flying and the temperature is dropping, will you make it before you become one with the cabin?

![](https://i.imgur.com/lnb4AQ1.png)

Flag: HTB{th1s_1s_th3_t1ny_3ncryp710n_4lg0r1thm_y0u_m1ght_h4v3_4lr34dy_s7umbl3d_up0n_1t_1f_y0u_d0_r3v3rs1ng}

#ctf #crypto 

---
Given 2 file, one output and one source as shown below. 
##### Output.txt
```
Key : 850c1413787c389e0b34437a6828a1b2
Ciphertext : b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843
```
##### Source.py
```python
import os
from secret import FLAG
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum

class Mode(Enum):
    ECB = 0x01
    CBC = 0x02

class Cipher:
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        if self.IV:
            self.mode = Mode.CBC
        else:
            self.mode = Mode.ECB
    
    def _xor(self, a, b):
        return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

    def encrypt(self, msg):
        msg = pad(msg, self.BLOCK_SIZE//8)
        blocks = [msg[i:i+self.BLOCK_SIZE//8] for i in range(0, len(msg), self.BLOCK_SIZE//8)]
        
        ct = b''
        if self.mode == Mode.ECB:
            for pt in blocks:
                ct += self.encrypt_block(pt)
        elif self.mode == Mode.CBC:
            X = self.IV
            for pt in blocks:
                enc_block = self.encrypt_block(self._xor(X, pt))
                ct += enc_block
                X = enc_block
        return ct

    def encrypt_block(self, msg):
        m0 = b2l(msg[:4])
        m1 = b2l(msg[4:])
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        s = 0
        for i in range(32):
            s += self.DELTA
            m0 += ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            m1 += ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk
        
        m = ((m0 << (self.BLOCK_SIZE//2)) + m1) & ((1 << self.BLOCK_SIZE) - 1) # m = m0 || m1

        return l2b(m)



if __name__ == '__main__':
    KEY = os.urandom(16)
    cipher = Cipher(KEY)
    ct = cipher.encrypt(FLAG)
    with open('output.txt', 'w') as f:
        f.write(f'Key : {KEY.hex()}\nCiphertext : {ct.hex()}')


```

By the name of the challenge, I begin with searching "Iced Tea encryption" on Google and I found out a Wiki [page](https://en.wikipedia.org/wiki/XTEA) explaining the eXtended Tiny Encryption Algorithm. The cipher code was similar to the one provided 
![](https://i.imgur.com/CVNLPh4.png)

I used ChatGPT to help me understand the code and come with the following script to decrypt the flag.
```python
from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum
import os

class Mode(Enum):
    ECB = 0x01
    CBC = 0x02

class Cipher:
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        if self.IV:
            self.mode = Mode.CBC
        else:
            self.mode = Mode.ECB
    
    def _xor(self, a, b):
        return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

    def decrypt(self, ct):
        blocks = [ct[i:i+self.BLOCK_SIZE//8] for i in range(0, len(ct), self.BLOCK_SIZE//8)]
        
        pt = b''
        if self.mode == Mode.ECB:
            for ct_block in blocks:
                pt += self.decrypt_block(ct_block)
        elif self.mode == Mode.CBC:
            X = self.IV
            for ct_block in blocks:
                pt_block = self._xor(X, self.decrypt_block(ct_block))
                pt += pt_block
                X = ct_block
        return pt

    def decrypt_block(self, ct):
        c = b2l(ct)
        m0 = c >> (self.BLOCK_SIZE//2)
        m1 = c & ((1 << (self.BLOCK_SIZE//2)) - 1)
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        s = self.DELTA << 5
        for i in range(32):
            m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk
            m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            s -= self.DELTA
        
        m = ((m0 << (self.BLOCK_SIZE//2)) + m1) & ((1 << self.BLOCK_SIZE) - 1) # m = m0 || m1

        return l2b(m)

# Parse Key and Ciphertext from file
with open('output.txt', 'r') as f:
    lines = f.readlines()
    KEY = bytes.fromhex(lines[0].split(":")[1].strip())
    ct_hex = lines[1].split(":")[1].strip()

# Initialize Cipher object with Key
cipher = Cipher(KEY)

# Decrypt Ciphertext
ct = bytes.fromhex(ct_hex)
pt = cipher.decrypt(ct)

# Remove Padding
pt = unpad(pt, cipher.BLOCK_SIZE//8)

print("Decrypted plaintext:", pt.decode())

```

![](https://i.imgur.com/0zpz8CT.png)
