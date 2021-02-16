from vidstream import StreamingServer
import threading


#enter your local wifi public ip and port
host = "127.0.0.1"
port = 55555

receiver = StreamingServer(host,port)

receiver_threading = threading.Thread(target=receiver.start_server)
receiver_threading.start()
print("Server is listening.....")

while input("") != 'STOP':
    continue

receiver.start_server()