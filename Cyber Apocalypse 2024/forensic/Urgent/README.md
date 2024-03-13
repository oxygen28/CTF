# Urgent
> In the midst of Cybercity's "Fray," a phishing attack targets its factions, sparking chaos. As they decode the email, cyber sleuths race to trace its source, under a tight deadline. Their mission: unmask the attacker and restore order to the city. In the neon-lit streets, the battle for cyber justice unfolds, determining the factions' destiny.

![](https://i.imgur.com/oOTGsaH.png)

Flag: HTB{4n0th3r_d4y_4n0th3r_ph1shi1ng_4tt3mpT}

#ctf #forensic #eml #javascript #obfuscation 

---
The files given for this challenge was a file Electric Mail Format file extension. I then search for more information about this file extension and I came across [emlAnalyzer](https://github.com/wahlflo/eml_analyzer)tool to view the content of the EML file and also extracting data from it.

After installing the tool, I started reading the help guide and learn how to use the tool. I first started analyze the file and found out that there's a HTML attachment.
![](https://i.imgur.com/Dm2zJAS.png)

Upon further reading on the help guide, the emlAnlayzer can also extract the attachment from the EML file. So I proceed to extract the HTML file out.
![](https://i.imgur.com/cq5DHJA.png)

I then open the extracted HTML file in the browser but it shows 404 Not Found. I then proceed to view the source of the HTML file itself and found something.
![](https://i.imgur.com/rgtUCtI.png)

It is an encoded JavaScript code. Since the code was not heavily obfuscated I can easily decode the encoded script.
![](https://i.imgur.com/O0Ywbk4.png)

I just use the console of the browser and use the `console.log()` and `unescape()` function to obtain the flag.
![](https://i.imgur.com/DgZ5qdL.png)

I also noticed that the flag can be obtained via the Inspect Element tool of the browser.![](https://i.imgur.com/XLmoy4R.png)

Other than that, I also found out that the EML file is an ASCII text file and I output the content of the file and got a Base64 encoded data of the attachment.
![](https://i.imgur.com/QxvQ5uh.png)

![](https://i.imgur.com/J3sPuCw.png)

I proceed to use [CyberChef](https://gchq.github.io/CyberChef/)to decode the Base64 data, and I obtained the same value as when I view the page source of the HTML file.
![](https://i.imgur.com/wDZqjns.png)