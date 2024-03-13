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

print("HTB{"+decrypt(flag)+"}")
