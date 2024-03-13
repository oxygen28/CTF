# Makeshift
> Weak and starved, you struggle to plod on. Food is a commodity at this stage, but you can’t lose your alertness - to do so would spell death. You realise that to survive you will need a weapon, both to kill and to hunt, but the field is bare of stones. As you drop your body to the floor, something sharp sticks out of the undergrowth and into your thigh. As you grab a hold and pull it out, you realise it’s a long stick; not the finest of weapons, but once sharpened could be the difference between dying of hunger and dying with honour in combat.

![](https://i.imgur.com/ffHvLnU.png)


Flag: HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}

#ctf #crypto 

---
For this challenge we are given an output file and a source file as below.
##### Output.txt
```
!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB
```
##### Source.py
```python
from secret import FLAG

flag = FLAG[::-1]
new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+1]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)

```

It is a simple algorithm which works as follow:
1. Inverse the value of the flag.
2. Create a variable called new_flag.
3. In a for loop, iterate every 3 step until it reached the end of the value of the flag and append the value in the order of *2nd*, *3rd*, and *1st* position. (Let's say there's a string of "ABC" the algorithm will append the string in such order "BCA").

| Pos | Original Value | Value After |
| --- | -------------- | ----------- |
| 1   | A              | B           |
| 2   | B              | C           |
| 3   | C              | A           |

After knowing that, I started writing the script to reverse the algorithm, which is by appending the value of the given string in the order of *3rd*, *1st*, and *2nd* position to obtain the value and inverse it to obtain the original flag.
```python
new_flag = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"
old_flag = ""
for i in range (0,len(new_flag),3):
	old_flag += new_flag[i+2]
	old_flag += new_flag[i]
	old_flag += new_flag[i+1]
	
print(old_flag[::-1])
```

![](https://i.imgur.com/W6Zpv3v.png)
