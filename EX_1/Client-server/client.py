#CH.SC.U4CSE24001 
import socket 
PORT = 12345 
SERVER_IP = input("Enter Server IP Address: ") 
# Create client socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
try: 
    client.connect((SERVER_IP, PORT)) 
    print("================================") 
    print("      CONNECTED TO SERVER") 
    print("================================") 
    print("Type 'exit' to end the chat.") 
    server_file = client.makefile("r") 
    while True: 
        # Send message to server 
        message = input("\nClient 24001: ") 
        client.sendall((message + "\n").encode()) 
        if message.lower() == "exit": 
            print("Chat ended.") 
            break
        reply = server_file.readline() 
        if not reply: 
            print("Server disconnected.") 
            break 
        reply = reply.strip() 
        print("Server:", reply) 
        if reply.lower() == "exit": 
            print("Server ended the chat.") 
            break 
finally: 

    client.close() 