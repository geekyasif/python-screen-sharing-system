from vidstream import StreamingServer
import threading

receiver = StreamingServer('192.168.1.11',9999)

receiver_threading = threading.Thread(target=receiver.start_server)
receiver_threading.start()
print("Server is listening.....")

while input("") != 'STOP':
    continue

receiver.start_server()