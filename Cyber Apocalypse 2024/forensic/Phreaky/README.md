# Phreaky
> In the shadowed realm where the Phreaks hold sway,
A mole lurks within, leading them astray.
Sending keys to the Talents, so sly and so slick,
A network packet capture must reveal the trick.
Through data and bytes, the sleuth seeks the sign,
Decrypting messages, crossing the line.
The traitor unveiled, with nowhere to hide,
Betrayal confirmed, they'd no longer abide.

![](https://i.imgur.com/arVPHF0.png)

Flag: HTB{Th3Phr3aksReadyT0Att4ck}

#ctf #forensic #pcap #pdf #wireshark 

---
The file given is a PCAP file, hence I opened it using WireShark to analyze it. First I open up the Capture File Properties to identify what am I dealing with.
![Capture File Properties](https://i.imgur.com/gL8arNf.png)

I then dig into the Protocol Hierarchy Statistics and found out that most of there's a huge portion in Internet Message Format and HTTP. So I then applied the filter to filter the IMF protocol first.
![](https://i.imgur.com/COmphmL.png)

I found out that there's plain text data of the password and also filename, and I noticed that the file type is in ZIP format. I then search online on how to extract file from WireShark and found [this](https://youtu.be/Fn__yRYW6Wo?si=Vb2-AJyLFGH5g4ID) video on YouTube which guide on how to export the data from WireShark. I also note down all of the filename and password for the extraction of data later.
![](https://i.imgur.com/ach8zqs.png)

I then proceed to export the file from WireShark and noticed that the content type of the exports are EML.
![](https://i.imgur.com/zvKPl9m.png)

I proceed to use the [emlAnalyzer](https://github.com/wahlflo/eml_analyzer) to extract the ZIP file from the all of the exported EML file from WireShark earlier.
![](https://i.imgur.com/FH7JMkp.png)

Here's where the filename and password from earlier comes in handy. I just pasted the password to extract the file for each of the ZIP file extracted and I got these PDF fragments.
![](https://i.imgur.com/BnRMY8U.png)

So, I just use a simple command to combine all these PDF fragments into one combined PDF file.
![](https://i.imgur.com/leZ7fFd.png)

After that, I open up the combined pdf and found the flag.
![](https://i.imgur.com/TWLzM2M.png)

