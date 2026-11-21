#CH.SC.U4CSE24001 

import socket 

import os 

import json 

HOST = "0.0.0.0" 

PORT = 12346 

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

SHARED_FOLDER = os.path.join(BASE_DIR, "SHARED_FOLDER") 

if not os.path.isdir(SHARED_FOLDER): 

    os.makedirs(SHARED_FOLDER) 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind((HOST, PORT)) 

server.listen(5) 

print("================================") 

print("       FILE SERVER STARTED") 

print("================================") 

print("Shared folder:", SHARED_FOLDER) 

print("Waiting for client requests...") 

try: 

    while True: 

        conn, addr = server.accept() 

        print("\nClient connected:", addr) 

        with conn: 

            files = [] 

            for item in os.scandir(SHARED_FOLDER): 

                if item.is_file(): 

                    files.append(item.name) 

            files.sort() 

            response = json.dumps(files) + "\n" 

            conn.sendall(response.encode()) 

            print("Files sent successfully:") 

            for filename in files: 

                print("-", filename) 

 

 

 

finally: 

    server.close() 