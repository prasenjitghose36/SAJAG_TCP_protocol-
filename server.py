import socket 
import threading

print("SAJAG TCP PROTOCOL\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("█▀ ▄▀█ ░░█ ▄▀█ █▀▀       ▀█▀ █▀▀ █▀█       █▀█ █▀█ █▀█ ▀█▀ █▀█ █▀▀ █▀█ █░░\n▄█ █▀█ █▄█ █▀█ █▄█       ░█░ █▄▄ █▀▀       █▀▀ █▀▄ █▄█ ░█░ █▄█ █▄▄ █▄█ █▄▄")
print("Project Lead:-\nPrasenjit Ghose 2nd Year Btech Computer Science and Engineering\nManasis Das 2nd Year Btech Electronics and Telecommunication Engineering\n\n\n\n")                                                                      

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
         
        
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("[STARTING] server is starting...")
start()
