# Ilmu Hisab
> Mampukah tuan hamba mengira?

![](https://i.imgur.com/lIEQzHF.png)

Flag: 3108{n0mb0r_k3r4mat}

#ctf #rev

---
We are given an ELF file to reverse and NetCat connection to get the actual flag.
![](https://i.imgur.com/FTdhG57.png)

Using [DogBolt](https://dogbolt.org/?id=1e45d5b6-d3ee-4bf3-ab36-d037be422064#Hex-Rays=272&BinaryNinja=240)we can look at the decompiled code. At which we would put our attention to the function `addtwonumber` which will accept two values where
`v9` = first value
`v10` = second value

![](https://i.imgur.com/k5dECPw.png)

Notice that the first highlighted If statement checks if the the value of `v9` is less than `MAX Numeric Limit - 83647`. 

Then the second highlighted If statement checks 
If the value of `v9` = 1337 AND `v10` greater than 7331 AND the sum of both value needs to be less than 0. (Impossible)
OR
If the value of `v9` less than 0 AND `v10` less than 0 AND sum of both more than 0 (Impossible)

The If statement seems to be impossible to achieve *merdeka* function. But not with Integer Overflow. (Watch this video: [Overflow in Signed and Unsigned Numbers](https://youtu.be/7towQUO9aZI?si=Zy4yzxgvuegIzmum&t=345))

To obtain merderka function. We can add `v9 + v10 > 2147483647` which is the *MAX Numeric Limit*. Using the first condition where `v9` = 1337 AND `v10` greater than 7331 to perform the overflow. Since we know that `v9` cannot be changed, we need to find `v10`.
`v10 = 2147483657 - 1336 = 2147482321`

With that we can reach *merdeka* function which will reveal the flag.
![](https://i.imgur.com/8hc7wYL.png)


