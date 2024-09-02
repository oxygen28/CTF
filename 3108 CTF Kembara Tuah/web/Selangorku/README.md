# Selangorku
> Hi semua saya @AnakSelangor86. Saya seorang Web Developer yang mempunyai semangat patriotik yang tinggi terhadap kemerdekaan terutamanya negeri selangor saya ada cipta satu website mengenai selangor dan hanya orang tertentu sahaja bole access ke website tersebut :)
> 
> selamat mencubaa perwira!!!!

![](https://i.imgur.com/iE1Y2Cm.png)


Flag: 3108{S3lang0r_temp4t_kelahiran_ku}

#ctf #web #forbidden

---
Trying to access the webpage will give us 403 Forbidden. I then go and search online for any possible solution and found this [writeup](https://ctftime.org/writeup/10788)
![](https://i.imgur.com/oHUurJq.png)

Then I tried using Curl with X-Forwarderd-For header to local host.
```
curl -v <url> -H 'X-Forwarded-For: 127.0.0.1'
```

Which I am able to access the site and it shows a list of html files. I tried to access it using the above method and found the flag at the hulu_selangor.html 
![](https://i.imgur.com/TqAi0FK.png)

![](https://i.imgur.com/vgdgHlh.png)

I found this to be quite similar and very helpful resource [Cyber Plumber Handbook](https://github.com/opsdisk/the_cyber_plumbers_handbook/blob/master/cph_version_1.4_20210829.pdf), which teach about ways to navigate around the network using SSH and port redirection.