# Mesej Rahsia
> Tak susah pun, run je script

![](https://i.imgur.com/wwH04a4.png)

Flag: 3108{substitute_cipher_text}  

#ctf #crypto 

---
For this challenge, we are given a python script.
##### secretMessenger.py
```python
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z='j','b','a','c','m','n','i','p','o','q','r','t','x','z','v','s','u','y','h','g','d','e','f','k','l','w'
flag=((3108,"{",p,q,b,p,l,g,l,q,l,v,"_",d,g,h,s,v,k,"_",l,v,m,l,"}")[::-1])
```

From the script we can see there's the flag variable set to the predefined variables in reverse.

Then what we can do is remove the slice notation and join the flag  and print it out. 
##### Solution.py
```python
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z='j','b','a','c','m','n','i','p','o','q','r','t','x','z','v','s','u','y','h','g','d','e','f','k','l','w'
flag="".join(str(i) for i in (3108,"{",p,q,b,p,l,g,l,q,l,v,"_",d,g,h,s,v,k,"_",l,v,m,l,"}"))
print(flag)
```

![](https://i.imgur.com/FpXb5wc.png)
