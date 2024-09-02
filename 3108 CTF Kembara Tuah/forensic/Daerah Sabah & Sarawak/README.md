# Daerah Sabah & Sarawak
> Setiap negeri mempunyai daerah. Begitu juga negeri Sabah dan Sarawak mempunyai daerah tersendiri. Cari 'flag' yang mengandungi bilangan daerah Sabah dan Sarawak di dalam file tersebut.

![](https://i.imgur.com/uQlH1Fg.png)

Flag: 3108{S4B4H_27_D43RAH_S4R4W4K_40_D43R4H} 

#ctf #forensic #steganography

---
We are given a zip file
![](https://i.imgur.com/caFKoMD.png)

Then I proceed to unzip the zip file and obtained 3 jpg file.
![](https://i.imgur.com/Xv3Hhlt.png)

These images does not show anything, so I tried to use [Stegoveritas](https://github.com/bannsec/stegoVeritas)to extract the *3.jpg* because it feels weird to have AI generated image to mix with the rest normal looking images. Also the file size seems to be larger than the rest that might indicate something is hidden within the image itself.
![](https://i.imgur.com/x1j2f7E.png)

![](https://i.imgur.com/CyuX0M3.png)

Stegoveritas managed to find an archived file hidden in the *3.jpg* extracted the file out.
![](https://i.imgur.com/0EIfvUQ.png)

I checked the file and it's a RAR archive file, I then proceed to extract the file and obtained a text file and a zip file.
![](https://i.imgur.com/TQ0XHUQ.png)

The *Daerah_Sabah&Sarawak.txt* contains the names of all the Town and City in Sabah and Sarawak.
![](https://i.imgur.com/pO2NqvE.png)

The *file.zip* however is AES encrypted. Which got me thinking that the given text file might be the wordlist that can be use for bruteforce.
![](https://i.imgur.com/7RZFhUB.png)

The password can be obtained by using *zip2john* and run JohnTheRipper using the wordlist above.
![](https://i.imgur.com/y5hGLFv.png)

After extracting the file, the flag can be obtained.
![](https://i.imgur.com/8qcnifm.png)
