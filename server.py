import socket
import threading

# message type
TRANSFER = 20
#  header at the start of the message coming from the user tell the size of message
HEADER = 64
# set the port to the server
PORT = 5050
# get tht IP address of the device
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# create socket(allow you to open the device up to other connections)
# socket.AF_INET: what type of IP address that we are looking for a specific connection
# socket.SOCK_STREAM: the way of sending data (streaming)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server socket to the address
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected.")

    connected = True
    while connected:
        transfer_type = conn.recv(TRANSFER).decode(FORMAT)
        if transfer_type.strip() == "message":
            print("[RECEIVING MESSAGE...]")
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                # get size of the message from the header
                msg_length = int(msg_length)
                # receive the actual message
                msg = conn.recv(msg_length).decode(FORMAT)
                print(f"[{addr} SAYS] {msg}")
                conn.send("[SERVER] message received".encode(FORMAT))

                # Disconnecting from the server
                if msg == DISCONNECT_MESSAGE:
                    print(f"[{addr}] !Disconnecting...")
                    connected = False

        elif transfer_type.strip() == "file":
            print("[RECEIVING FILE...]")
            file_name = conn.recv(1024).decode(FORMAT)
            print(f"[RECEIVED FILE NAME] {file_name}")

            file_name = "transferred " + file_name
            file = open(file_name, "w")
            file_length = int(conn.recv(HEADER).decode(FORMAT))
            print(f"[RECEIVED FILE LENGTH] {file_length}")

            file_content = conn.recv(file_length).decode(FORMAT)
            print(f"[RECEIVED FILE CONTENT] file content received.")
            file.write(file_content)
            file.close()
            print(f"[FILE SAVED]")
            conn.send("[SERVER] file received".encode(FORMAT))

        elif transfer_type.strip() == "image":
            print("[RECEIVING IMAGE...]")
            img_name = conn.recv(1024).decode(FORMAT)
            print(f"[RECEIVED IMAGE NAME] {img_name}")

            img_name = "transferred " + img_name

            img_length = int(conn.recv(HEADER).decode(FORMAT))
            print(f"[RECEIVED IMAGE LENGTH] {img_length}")

            img_data = conn.recv(img_length)
            print(f"[RECEIVED IMAGE CONTENT] image received.")

            image_file = open(img_name, "wb")
            image_file.write(img_data)

            image_file.close()
            print(f"[IMAGE SAVED]")
            conn.send("[SERVER] IMAGE received".encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on IP: {SERVER}, PORT: {PORT}")
    while True:
        # when we have a new connection we will store it's address and the port it com's from
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS] {}".format(threading.activeCount() - 1))


print("[STARTING] server is starting...")
start()

