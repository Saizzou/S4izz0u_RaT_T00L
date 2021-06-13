import socket
import tqdm
import os

SEPERATOR = "<SEPERATOR>"
BUFFERSIZE = 4096 # send 4kib steps

def file_transfer(filename, host, port):
    filesize = os.path.getsize(filename)
    s = socket.socket()
    #print(f"[+] Connecting to: {host}")
    s.connect((host,port))
    s.send(f"{filename}{SEPERATOR}{filesize}".encode())
    #print(f"[+]Connected to {host}!")
    progress = tqdm.tqdm(range(filesize),f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            #Read Bytes from the file!
            bytes_read = f.read(BUFFERSIZE)
            if not bytes_read:
                # File Transfer is done!
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))
    s.close() #Closing File Transfer connection!