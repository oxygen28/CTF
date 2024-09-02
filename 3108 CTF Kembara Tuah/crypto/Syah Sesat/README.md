# Syah Sesat
> Semasa Syah berada di Muzium Kota Kayang, dia telah menyaksikan sebuah persembahan Gambus yang dipersembahkan oleh seorang pemuzik dari Sabah yang berkunjung ke muzium tersebut. Lagu yang dipersembahkan ketika itu bertajuk Ampuk Ampuk Bulan. Kagum akan persembahan tersebut, beliau telah meninggalkan satu pesanan di bawah bersama kunci. Bolehkan anda merungkaikan pesanan tersebut dan mendapatkan Flag?
> 
> Cipher : }AYPF_KYMSOL_TOMMNG{8013EJVWASCUQOYOAGNURBETMYUIBMTNHGMALKGZTXUBDPS 
> Key : AMPUKAMPUKBULAN

![](https://i.imgur.com/DLPTEpF.png)

Flag: 3108{GAMBUS_BUDAYA_LAMA}

#ctf #crypto 

---
For this challenge, we are given a cipher text and a key.
##### Cipher Text
```
}AYPF_KYMSOL_TOMMNG{8013EJVWASCUQOYOAGNURBETMYUIBMTNHGMALKGZTXUBDPS
```
##### Key
```
AMPUKAMPUKBULAN
```

Given the cipher text and key, using [CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('AMPUKAMPUKBULAN')Reverse('Character')&input=fUFZUEZfS1lNU09MX1RPTU1OR3s4MDEzRUpWV0FTQ1VRT1lPQUdOVVJCRVRNWVVJQk1UTkhHTUFMS0daVFhVQkRQUw&oeol=FF) I tried to decode it using  Vigenère cipher and the output was noticeably reversed. So I reverse it and the flag can be seen.

![](https://i.imgur.com/i8iJjE3.png)
