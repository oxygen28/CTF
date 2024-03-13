# Stop Drop and Roll
> The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...

![](https://i.imgur.com/8ZyPfgM.png)

Flag: HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}

#ctf #misc #scripting #python 

---
Given a docker instance, I used `netcat` to access the docker instance and I am greeted with the prompt below.
![](https://i.imgur.com/FHih3Np.png)

![](https://i.imgur.com/KQqT1hJ.png)
I started to type in the response with the instruction given above, however I do feel like this is going to be tough by manually inputting the response. As the description of the challenge mentioned that the program would be repetitive. Therefore, my first thought would be creating a script to automate the response.

```python
import socket
import time

def play_game():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('83.136.254.167', 31113))  # Connect to the game server
        
        # Start the game
        data = s.recv(1024).decode()  # Receive initial message
        print(data)  # Print the initial message
        # Confirm readiness
        s.sendall(b'y\n')  # Send 'y' to confirm readiness
        time.sleep(1) # Delay before starting the confirmation
        
        # Repeat the response process until no data received.
        while True:
            data = s.recv(1024).decode()  # Receive game scenario
            if not data:  # If no data received, break the loop
                break
            print(data)  # Print the game scenario
            scenarios = data.strip().split(', ')  # Split the scenario into individual elements
            print("Scenarios:",scenarios)
            response = ""  # Initialize response string
            for scenario in scenarios:
                if "FIRE" in scenario:
                    response += "ROLL-"  # If scenario contains FIRE, append ROLL to response
                elif "GORGE" in scenario:
                    response += "STOP-"  # If scenario contains GORGE, append STOP to response
                elif "PHREAK" in scenario:
                    response += "DROP-"  # If scenario is PHREAK, append DROP to response
            response = response[:-1]  # Remove the last '-' from the response
            print("Response:", response)  # Print the response
            s.sendall(response.encode() + b'\n')  # Send the response to the server
            time.sleep(1) # Delay for 1 second
            

if __name__ == "__main__":
    play_game()  # Call the play_game function to start the game

```

![](https://i.imgur.com/eRKUFKP.gif)

After few minutes of running the script I got the flag.
![](https://i.imgur.com/hL6e7Cf.png)
