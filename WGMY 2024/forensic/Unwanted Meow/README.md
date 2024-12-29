# Unwanted Meow
> Uh.. Oh.. Help me, I just browsing funny cats memes, when I click download cute cat picture, the file that been download seems little bit wierd. I accidently run the file making my files shredded. Ughh now I hate cat meowing at me.
> 
> Hint: We don't want meow here.

![](https://i.imgur.com/e1NxOCf.png)

Flag: WGMY{4a4be40c96ac6314e91d93f38043a634}

#ctf #forensic #image

---
We are given a file named `flag.shredded`, which is a JPEG image file, but it appears to be corrupted.

![](https://i.imgur.com/BwbqBNV.png)

After opening the file in a text editor, it can be seen that the word `meow` is repeatedly placed throughout the file. To recover the image, I removed the `meow` entries and then added the `.jpeg` extension to the file.
![](https://i.imgur.com/Bcs2mil.png)

After this, the recovered image is still partially corrupted. To repair it, I used [JPEG Medic](https://www.jpegmedic.com/tools/jpegmedic/) to fix the image.

![](https://i.imgur.com/bbQbMLF.png)

After tinkering with JPEG Medic for a while, I was able to see part of the flag, even though the image was not fully recovered. The flag was visible in the partially restored image.

![](https://i.imgur.com/dEALXr4.png)

Upon reviewing other writeups for this challenge, I realized that the intended solution was actually hidden in plain sight, which I had not noticed earlier. Instead of repairing the image, the flag could have been obtained simply by removing the additional `meow` entries and viewing the image directly.

![](https://i.imgur.com/c1YkbOg.png)

After removing the second set of `meow` entries, the image was fully recovered, and the flag can be successfully obtained.

![](https://i.imgur.com/MJT8JWj.jpeg)