#CH.SC.U4CSE24001 

import socket 

HOST = "0.0.0.0" 

PORT = 12345 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind((HOST, PORT)) 

server.listen(1) 

 

print("================================") 

print("       CHAT SERVER STARTED") 

print("================================") 

print("Waiting for client connection...") 

 

conn, addr = server.accept() 

 

print("Client 24001 connected from:", addr) 

 

try: 

    while True: 

        # Receive message from client 

        message = conn.makefile("r").readline() 

        if not message: 
            print("Client 24001 disconnected.") 
            break 
        message = message.strip() 
        print("\nClient 24001:", message) 
        if message.lower() == "exit": 
            print("Client 24001 ended the chat.") 
            break 
        # Send reply to client 
        reply = input("Server: ") 
        conn.sendall((reply + "\n").encode()) 
        if reply.lower() == "exit": 

            print("Chat ended.") 

            break 

 

finally: 

    conn.close() 

 

    server.close() 

    print("Server closed.") 