import socket
import threading


MY_IP = "127.0.0.1" #---> loaclhost 
MY_PORT = 12346 # isko uske sth se badalna hai

PEER_IP = "127.0.0.1"
PEER_PORT = 12345  #isko exnchage krna hai 

def receive_messages(sock):
    while True:
        try:
            message, addr = sock.recvfrom(1024)
            print(f"\nFriend ({addr}): {message.decode()}")
        except:
            break

def main():
    # UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((MY_IP, MY_PORT))
    print(f"Listening on {MY_IP}:{MY_PORT}...")

    # Start receiving thread
    recv_thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    recv_thread.start()

    # Send messages
    while True:
        msg = input("You: ")
        if msg.lower() in ['exit', 'quit']:
            print("Exiting chat.")
            break
        sock.sendto(msg.encode(), (PEER_IP, PEER_PORT))

    sock.close()

if __name__ == "__main__":
    main()
