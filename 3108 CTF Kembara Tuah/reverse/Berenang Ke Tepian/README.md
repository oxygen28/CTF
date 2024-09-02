# Berenang Ke Tepian
> Berakit, berakitlah ke hulu Berenang, berenangku ke tepian Bersakit, biar kusakit dahulu Bersenang denganmu kemudian
> 
> Kelip-kelip kusangkakan api Sinar matahari membawa cahaya Kau hilang ghaib, sangkaku kaubenci Kiranya sengaja nak menduga

![](https://i.imgur.com/jUftMDS.png)

Flag: 3108{s1mpl3_p3ngundur4n}

#ctf #rev

---
We are given an ELF executable and the NetCat connection to obtain the real flag.
![](https://i.imgur.com/i8MJf2W.png)

I uploaded the binary to DogBolt to decompile to understand the code and found something interesting. Which is the *Sleep* timer that is being applied given that the character is correct. If the character is wrong, then it will terminate without the *Sleep* timer being imposed. That means, we can exploit this functionality to brute-force the flag, this exploit is also known as Side Channel Attack (watch this [video](https://youtu.be/YRohz9VO1YY?si=P5032ZUSKD6Peuqq) to understand side channel attack)

![](https://i.imgur.com/sYTFw1z.png)

Now knowing that I asked ChatGPT to help me create a script to perform the attack. I set the flag length to 100 because I'm not sure how long the flag was and I just did it the "dirty" way. The brute-force process took a long time, there should be better solution to this.
```python
import socket
import time
import string

def send_input_and_measure_time(input_string, remote_ip, remote_port):
    """Send input to the remote service and measure the time taken for a response."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((remote_ip, remote_port))
        s.sendall((input_string + '\n').encode())
        
        start_time = time.perf_counter()
        response = receive_response(s)
        end_time = time.perf_counter()
        
        response_time = end_time - start_time
        
    finally:
        s.close()
    
    return response_time, response

def receive_response(sock):
    """Receive the full response from the server."""
    response = b''
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk
        if b'\n' in response:
            break
    return response.decode()

def find_flag_character(position, current_flag, remote_ip, remote_port):
    """Determine the best character for the given position in the flag."""
    characters = string.ascii_letters + string.digits + string.punctuation
    best_char = ''
    max_time = 0
    
    for char in characters:
        guess = current_flag + char
        response_time, _ = send_input_and_measure_time(guess, remote_ip, remote_port)
        if response_time > max_time:
            max_time = response_time
            best_char = char
    
    return best_char

def recover_flag(remote_ip, remote_port, known_prefix):
    """Recover the full flag by guessing each character, starting from a known prefix."""
    flag = known_prefix
    flag_length = 100  # Initial guess for the length of the flag
    
    for i in range(len(known_prefix), flag_length):
        flag += find_flag_character(i, flag, remote_ip, remote_port)
        print(f"Flag so far: {flag}")
    
    print(f"Recovered Flag: {flag}")

# Example usage
remote_ip = '103.28.91.24'  # Remote IP address
remote_port = 10020          # Remote port
known_prefix = "3108{"  # Known initial part of the flag
recover_flag(remote_ip, remote_port, known_prefix)
```

The flag can be obtained after the brute-force process finished.

![](https://i.imgur.com/lwCJ9xj.png)
