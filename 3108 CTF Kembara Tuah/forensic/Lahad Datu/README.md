# Lahad Datu
> Scott seorang bangsa Melayu kacukan darah British ingin mengetahui peristiwa hitam yang berlaku di Sabah yang ada di dalam dokumen "Lahad Datu". Tetapi dokumen tersebut mempunyai kata laluan. Bantu Scott untuk membuka dokumen berkenaan.

![](https://i.imgur.com/mMc7GNB.png)

Flag: 3108{0P3R4S1_D4UL4T}

#ctf #doc #forensic 

---
We are given an encrypted Word document. 
![](https://i.imgur.com/smeTOEU.png)

Without any hint given,  I tried to brute-force the password using JohnTheRipper with common wordlist. The brute-force process was rather quick and I used the password to open the Word document.
![](https://i.imgur.com/5Sp1Eky.png)

![](https://i.imgur.com/Rc6u1A5.png)

There's the flag at the bottom, but is it the real flag? Seems like gibberish to me, hence I notice the *JamalulKiramIII* that was bolded and thought that it might be used to decode the flag. So I go over to trusty [CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('JamalulKiramIII')&input=MzEwOHswWTNSNEUxX0Q0RkY0RX0)and used the Vigenère module to decode the flag.
![](https://i.imgur.com/Lh5U7XS.png)
