# Sarawak Kita
> Ada pendapat yang menyatakan bahawa Kuching mendapat nama sempena sebatang sungai kecil, Sungai Kuching yang mengalir di antara Muzium Cina dan Kuil Tua Pek Kong. Sungai Kuching pula barangkali memperoleh nama daripada Kucing Hutan yang kerap mengunjunginya. Sungai tersebut juga berhampiran dengan sebuah bukit yang banyak ditumbuhi oleh pokok Buah Mata Kucing. Lantaran tersebut ianya diberi nama Bukit Mata Kucing. Tapi ini bukan tentang kisah Kuching, ini kisah bagaimana ingin mendapatkan 'flag' di dalam document yang berbahaya.

![](https://i.imgur.com/dcU2nVK.png)

Flag: 3108{Kuch1ng_1bu_N3g3r1_S4r4w4k}

#ctf #rev

---
We are given a Word Document, using [oleid](https://github.com/decalage2/oletools/wiki/oleid)it can be seen that the document contains VBA macros
![](https://i.imgur.com/ZDUpAGV.png)

With that I used [olevba](https://github.com/decalage2/oletools/wiki/olevba) to read the VBA code, and found a Base64 hash
![](https://i.imgur.com/OlwJFZV.png)

As always I will use the trusty [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Remove_null_bytes()&input=TXdBeEFEQUFPQUI3QUVzQWRRQmpBR2dBTVFCdUFHY0FYd0F4QUdJQWRRQmZBRTRBTXdCbkFETUFjZ0F4QUY4QVV3QTBBSElBTkFCM0FEUUFhd0I5QUE9PQ) to decode the Base64 and obtained the flag.
![](https://i.imgur.com/hc4crqg.png)

This [article](https://intezer.com/blog/malware-analysis/analyze-malicious-microsoft-office-files/)from Intezer explains in detail how to analyze Microsoft Office files.