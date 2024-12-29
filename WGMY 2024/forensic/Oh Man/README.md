# Oh Man
> We received a PCAP file from an admin who suspects an attacker exfiltrated sensitive data. Can you analyze the PCAP file and uncover what was stolen?
> 
> Zip Password: `wgmy`
> 
> Hint: Investigate the tool used by the attacker

![](https://i.imgur.com/0s6npML.png)

Flag: wgmy{fbba48bee397414246f864fe4d2925e4}

#ctf #forensic #pcap #wireshark 

---
We are given a `PCAP` file containing encrypted SMB traffic. Our goal is to decrypt the SMB traffic in order to obtain the transferred file. After researching online, I found this [write-up](https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2) that explains how to decrypt SMB traffic.

![](https://i.imgur.com/OMbWMmd.png)

**What We Need to Decrypt the SMB Traffic**
To decrypt the traffic from the `PCAP` file, we need the following information:
1. **Domain**
2. **Username**
3. **Password/NTLM Hash** (can be cracked)
4. **NTProofStr**
5. **NTLM Server Challenge**
6. **Encrypted Session Key**
7. **Session ID**

### 1. Obtain the data from the Session Setup Packet
From the _Session Setup Request, NTLMSSP_AUTH_ packet, we can extract the following data:
- **Domain**: `DESKTOP-PMNU0JK`
- **Username**: `Administrator`
- **Encrypted Session Key**: `12140eb776cb74a339c9c75b152c52fd`

![](https://i.imgur.com/TrXvDay.png)

Next, we extract the **NTProofStr** and the remaining **NTLM Response Data**:
- **NTProofStr**: `ae62a57caaa5dd94b68def8fb1c192f3`
- **Remaining NTLM Response Data**: `01010000000000008675779b2e57db01376f686e57504d770000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b00070008008675779b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000`

![](https://i.imgur.com/kuT6B27.png)

- **Session ID**: `65000000000c0000`
  To convert this, use [CyberChef](https://cyberchef.org/#recipe=Swap_endianness('Hex',8,true)Remove_whitespace(true,true,true,true,true,false) &input=MHgwMDAwMGMwMDAwMDAwMDY1) to swap the endianness.

![](https://i.imgur.com/UsAEOKs.png)

From the _Session Setup Response, NTLMSSP_CHALLENGE_ packet, we obtain the **NTLM Server Challenge**:
- **NTLM Server Challenge**: `7aaff6ea26301fc3`

![](https://i.imgur.com/gJBZwxg.png)

### 2. Crack the Password Using the NTLM Data
Now that we have all the required data, we can construct the hash to crack the password using HashCat. The format is:
`Username::Domain:NTLMServerChallenge:NTProofStr:RemainingNTLMResponseData`
##### Hash
```
Administrator::DESKTOP-PMNU0JK:7aaff6ea26301fc3:ae62a57caaa5dd94b68def8fb1c192f3:01010000000000008675779b2e57db01376f686e57504d770000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b00070008008675779b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
```

Once the hash is constructed, you can use HashCat to crack the password. The cracked password is `password<3`.

![](https://i.imgur.com/1T1jp2I.png)

### 3. Obtain the Random Session Key
With the data obtained from the packet and the cracked password, we can calculate the random session key using the following Python script:
##### Get Random Session Key.py
```python
import hashlib
import hmac
import argparse

try:
    from Cryptodome.Cipher import ARC4
    from Cryptodome.Cipher import DES
    from Cryptodome.Hash import MD4
except Exception:
    print("Warning: You don't have any crypto installed. You need pycryptodomex")
    print("See https://pypi.org/project/pycryptodomex/")

def generateEncryptedSessionKey(keyExchangeKey, exportedSessionKey):
    cipher = ARC4.new(keyExchangeKey)
    cipher_encrypt = cipher.encrypt
    sessionKey = cipher_encrypt(exportedSessionKey)
    return sessionKey

parser = argparse.ArgumentParser(description="Calculate the Random Session Key based on data from a PCAP (maybe).")
parser.add_argument("-u", "--user", required=True, help="User name")
parser.add_argument("-d", "--domain", required=True, help="Domain name")
parser.add_argument("-p", "--password", required=True, help="Password of User")
parser.add_argument("-n", "--ntproofstr", required=True, help="NTProofStr. This can be found in PCAP (provide Hex Stream)")
parser.add_argument("-k", "--key", required=True, help="Encrypted Session Key. This can be found in PCAP (provide Hex Stream)")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

args = parser.parse_args()

user = str(args.user).upper().encode('utf-16le')
domain = str(args.domain).upper().encode('utf-16le')

# Create 'NTLM' Hash of password
passw = args.password.encode('utf-16le')
hash1 = hashlib.new('md4', passw)
password = hash1.digest()

# Calculate the ResponseNTKey
h = hmac.new(password, digestmod=hashlib.md5)
h.update(user + domain)
respNTKey = h.digest()

# Use NTProofSTR and ResponseNTKey to calculate Key Exchange Key
NTproofStr = bytes.fromhex(args.ntproofstr)
h = hmac.new(respNTKey, digestmod=hashlib.md5)
h.update(NTproofStr)
KeyExchKey = h.digest()

# Calculate the Random Session Key by decrypting Encrypted Session Key with Key Exchange Key via RC4
RsessKey = generateEncryptedSessionKey(KeyExchKey, bytes.fromhex(args.key))

if args.verbose:
    print("USER WORK: " + user.decode('utf-16le') + " " + domain.decode('utf-16le'))
    print("PASS HASH: " + password.hex())
    print("RESP NT:   " + respNTKey.hex())
    print("NT PROOF:  " + NTproofStr.hex())
    print("KeyExKey:  " + KeyExchKey.hex())    

print("Random SK: " + RsessKey.hex())
```

Running the script with the correct parameters gives us the **Random Session Key**: `4147454a48564a4373437649574e504c`

![](https://i.imgur.com/rDZlwZC.png)

### 4. Decrypt the SMB Traffic in WireShark
To decrypt the SMB traffic in Wireshark:
Go to `Edit > Preferences > Protocols > SMB2 > Secret session keys for decryption > Edit`

![](https://i.imgur.com/4ch2cHi.png)

### 5. Extract the files
Once decrypted, we can extract the files using:
`File > Export Objects > SMB > Save All`

![](https://i.imgur.com/IbkE8cP.png)

### 6. Analyze the Extracted Files
##### wqpiZo
```
"lsass.exe","840","Services","0","24,332 K","Unknown","NT AUTHORITY\SYSTEM","0:00:00","N/A"
```

##### RxHmEj
```
The minidump has an invalid signature, restore it running:
scripts/restore_signature 20241225_1939.log
Done, to get the secretz run:
python3 -m pypykatz lsa minidump 20241225_1939.log

python3 -m pypykatz lsa minidump 20241225_1939.log
```

##### 20241225_1939.log

![](https://i.imgur.com/5E99tbB.png)

##### nano.exe
This is identified as `nanodump.exe` from [VirusTotal Scan](https://www.virustotal.com/gui/file/bc21f289cc113a77ca1f48900a321d8f0eff024634a9255becc8afda66c213bd/details), which can be found on [GitHub](https://github.com/fortra/nanodump).

Now we know that the `20241225_1939.log` can be used to get the minidump, then the next step is to restore the log file as the signature seems to be invalid MiniDump log file.

The method I used to restore is by downloading the `scripts/restore_signature` from the [NanoDump's GitHub](https://github.com/fortra/nanodump)  and run the script on the log file.

![](https://i.imgur.com/sXp9ZeW.png)

### 7. Get the flag
The flag can be obtained by running the pypykatz module and read the mini dump.

![](https://i.imgur.com/Qhwswlj.png)