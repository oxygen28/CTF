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
