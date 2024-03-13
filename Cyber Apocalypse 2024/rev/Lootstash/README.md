# Lootstash
> A giant stash of powerful weapons and gear have been dropped into the arena - but there's one item you have in mind. Can you filter through the stack to get to the one thing you really need?

![](https://i.imgur.com/hYdh5QO.png)

Flag: HTB{n33dl3_1n_a_l00t_stack}

#ctf #rev #elf 

---
The file given is an ELF file, and the description of the challenge mentioned about filter through the stack.
![](https://i.imgur.com/kAwo7M1.png)

So what I did was using `strings` to get the string value of the file and use `grep` to filter the keyword of the flag which is HTB and that is how I obtained the flag.
![](https://i.imgur.com/1EmmLHI.png)
