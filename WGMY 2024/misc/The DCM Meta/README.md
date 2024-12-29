# The DCM Meta
> [25, 10, 0, 3, 17, 19, 23, 27, 4, 13, 20, 8, 24, 21, 31, 15, 7, 29, 6, 1, 9, 30, 22, 5, 28, 18, 26, 11, 2, 14, 16, 12]
> 
> Hint: The element is the number in the list, combine for the flag. Wrap in wgmy{}

![](https://i.imgur.com/B2Gc7oG.png)

Flag: WGMY{51fadeb6cc77504db336850d53623177}

#ctf #misc 

---
We are given a file with a `.dcm` extension, but the file itself only contains data.

![](https://i.imgur.com/WyD3cJj.png)

I used [CyberChef](https://cyberchef.org/#recipe=Regular_expression('User%20defined','%5C%5Cw',true,true,false,false,false,false,'List%20matches') to extract all the words. From the indices provided in the description, the largest index is 31, which indicates that the data can only have 32 characters. Therefore, I also removed the padding `WGMY`. The extracted data is: `f63acd3b78127c1d7d3e700b55665354`

![](https://i.imgur.com/PjiUmHs.png)

Next, to obtain the actual flag, we use the indices provided in the challenge description: `[25, 10, 0, 3, 17, 19, 23, 27, 4, 13, 20, 8, 24, 21, 31, 15, 7, 29, 6, 1, 9, 30, 22, 5, 28, 18, 26, 11, 2, 14, 16, 12]`

By following these indices, we can rearrange the characters in the extracted string. To automate this process, I create a Python script:
##### flag.py
```python
element = "f63acd3b78127c1d7d3e700b55665354"
indices = [25, 10, 0, 3, 17, 19, 23, 27, 4, 13, 20, 8, 24, 21, 31, 15, 7, 29, 6, 1, 9, 30, 22, 5, 28, 18, 26, 11, 2, 14, 16, 12]

result = ''.join([element[i] for i in indices])

print("WGMY{"+result+"}")
```

![](https://i.imgur.com/PwjvaGM.png)

Fun Fact: 
*I asked ChatGPT to help me rearrange the extracted string using the indices provided. Unfortunately, I trusted ChatGPT without verifying the result, as it turns out, the output it provided was incorrect. Lesson learned: don't trust ChatGPT too much 😂*

![](https://i.imgur.com/5iUCmKQ.png)
