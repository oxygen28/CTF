# Credentials
> We found a leak of a blackmarket website's login credentials. Can you find the password of the user osman and successfully decrypt it?
> 
> Hint: The first user in user.txt corresponds to the first password in passwords.txt

![](https://i.imgur.com/bqzzlnG.png)

Flag: WGMY{b6d180d9c302d8a8daad1f2174a0b212}

#ctf #crypto 

---
For this challenge there are 2 files provided `passwd.txt` and `user.txt`.
##### user.txt
```text
osman
```
##### passwd.txt
```text
ZJPB{e6g180g9f302g8d8gddg1i2174d0e212}
```

I search for user `osman` from the `user.txt` which appeared on line 337.  On the `passwd.txt` file's line 337, I found the corresponding password for the user `osman` which is `ZJPB{e6g180g9f302g8d8gddg1i2174d0e212}`. 

This password appears to be encoded using ROT13. To decode it, I used [CyberChef ROT13 Brute Force](https://cyberchef.org/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'wgmy')&input=WkpQQntlNmcxODBnOWYzMDJnOGQ4Z2RkZzFpMjE3NGQwZTIxMn0)to decode it, with the known plaintext of `wgmy`.
 
![](https://i.imgur.com/Mbm5Fpz.png)
