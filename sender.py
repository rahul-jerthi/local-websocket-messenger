#CLI chat app, 

import socket

try:
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #dgram ---> message transfer
    #ip address -- ipv4 --- afinet -- adress family
    print("Socket is suddefully conected")
    
    
    IP = "Enter the ip"
    PORT = "<PORT NUMBER>"
    
    target_address = (IP,PORT)
    message = input("Enter your message: ")
    encoded_message = message.encode("ascii")
    client.sendto(encoded_message, target_address)
    print("Message sent to the server")
    client.close()
    
except Exception as e:
    print("An error occured", e)    
    