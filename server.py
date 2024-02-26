import socket 
from threading import Thread

from pynput.mouse import Button, Controller
from screeninfo import get_monitors
import autopy

SERVER = None
PORT = 8000
IP_ADDRESS = input( "Enter your computer IP ADDR:").strip()
screen_height = None
screen_width = None

mouse = Controller()

def setup():
    print("Welcome To Remote Mouse")
    global SERVER 
    global PORT 
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)
    getDeviceSize()

    print("\t\t\t SERVER IS WAITING FOR INCOMMING CONNECCTIONS")
    acceptConnections()
    
def acceptConnections():
    global SERVER
    
    while True:
        client_socket, addr = SERVER.accept( )
        print("connection established  with (client_socket) : {addr}")
    
def getDeviceSize():
    global screen_width
    global screen_height
    
    
    for m in get_monitor():
        sccreen_width = int(str(m).split("."))
        sccreen_height = int(str(m).split("."))