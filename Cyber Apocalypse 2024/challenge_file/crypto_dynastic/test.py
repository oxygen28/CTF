from random import randint

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)
    
def decrypt(ciphertext):
    m = ''
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if not ch.isalpha():
            dch = ch
        else:
            chi = to_identity_map(ch)
            dch = from_identity_map(chi - i)
        m += dch
    return m

ciphertext = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"
decrypted_flag = decrypt(ciphertext)
print("Decrypted FLAG:", decrypted_flag)
