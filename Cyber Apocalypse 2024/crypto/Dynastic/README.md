# Dynastic
> You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked. Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood. Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!

![](https://i.imgur.com/AafS5aD.png)

Flag: HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}

#ctf #crypto 

---
For this challenge, there are 2 files. The output file and also the source code.
##### Output.txt
```txt
Make sure you wrap the decrypted text with the HTB flag format :-]
DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL
```
##### Source.py
```python
from secret import FLAG
from random import randint

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c

with open('output.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(encrypt(FLAG))
```

This is a simple algorithm to encrypt the data. Here's how it works:
1. It will iterate through all of the data one by one.
2. Check if the character is alphabet letters, 
   - *True*: Minus the hex value of that ASCII character with 0x41, and then get the value of modulo 26 of the minus value and add 0x41 to it. After that, add the value with the current number of iteration. Then append the value into a variable X.
   - *False*: Append that value into a variable X.
3. Append the value from above into the variable Crypt.
4. Return the value Crypt.

The solution is very simple, just by reversing the steps used to encrypt the flag and the flag can be obtained.
##### Solution.py
```python
#from secret import FLAG
#from random import randint

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha(): # If not a character
            ech = ch
        else: #If it's a character
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c

def decrypt(flag):
	unencrypted_text = ''
	for i in range(len(flag)):
		char = flag[i]
		if not char.isalpha():
			dchar = char
		else:
			ichar = to_identity_map(char)
			dchar = from_identity_map(ichar - i)
		unencrypted_text += dchar
	return unencrypted_text

#with open('output.txt', 'w') as f:
#    f.write('Make sure you wrap the decrypted text with the HTB flag #format :-]\n')
#    f.write(encrypt(FLAG))
flag = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"

print("HTB{".decrypt(flag)."}")
```

![](https://i.imgur.com/TvLpwXw.png)
