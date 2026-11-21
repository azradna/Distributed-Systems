#CH.SC.U4CSE24001 
import socket 
import json 
# Server configuration 
PORT = 12346 
SERVER_IP = input("Enter File Server IP Address: ") 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
try: 
    # Connect to file server 
    client.connect((SERVER_IP, PORT)) 
    print("\nConnected to File Server!") 
    # Receive file list 
    server_file = client.makefile("r") 
    data = server_file.readline() 
    if not data: 
        print("No response received from server.") 
    else: 
        files = json.loads(data) 
        print("\n================================") 
        print("        FILES AVAILABLE") 
        print("================================") 
        if len(files) == 0: 
            print("No files found in the shared folder.") 
        else: 
            for index, filename in enumerate(files, start=1): 
                print(f"{index}. {filename}") 
        print("================================") 
finally: 
    client.close() 
    print("Connection closed.") 