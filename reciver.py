import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Reciver socket created")
    
    IP = "Enter the ip"
    PORT = "<PORT NUMBER>"
    
    complete_add = (IP,PORT)
    client.bind(complete_add)
    
    while True:
        message , sender_address = client.recvfrom(1024)
        print(f"Received message from {sender_address}: {message.decode()}")
        
        #adding a file to store the messages --->>
        # with open('output.txt', "a") as f:
        #     f.write(message.decode() + "\n")

        
        

except Exception as e:
    print(f"Error: {e}")





