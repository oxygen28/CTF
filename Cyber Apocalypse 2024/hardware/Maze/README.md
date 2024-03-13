# Maze
> In a world divided by factions, "AM," a young hacker from the Phreaks, found himself falling in love with "echo," a talented security researcher from the Revivalists. Despite the different backgrounds, you share a common goal: dismantling The Fray. You still remember the first interaction where you both independently hacked into The Fray's systems and stumbled upon the same vulnerability in a printer. Leaving behind your hacker handles, "AM" and "echo," you connected through IRC channels and began plotting your rebellion together. Now, it's finally time to analyze the printer's filesystem. What can you find?

![](https://i.imgur.com/dEo19eF.png)

Flag: HTB{1n7323571n9_57uff_1n51d3_4_p21n732}

#ctf #hardware

---
Given the file system to the printer. I first list out the directories of the file system to see what folders do I have.
![](https://i.imgur.com/MCd5xNT.png)

The saveDevice seems to be interesting folder and might hold some data used by the to printer documents. Hence, I started digging into the the directory.
![](https://i.imgur.com/m1zue9E.png)

I came across this PDF file while digging through the file system and I opened it with a PDF viewer and managed to find the flag in the PDF.
![[Pasted image 20240310035535.png]]