from vidstream import ScreenShareClient
import threading

#enter your local wifi public ip and port
host = "127.0.0.1"
port = 55555

sender = ScreenShareClient(host,port)
sender_thread = threading.Thread(target=sender.start_stream)

sender_thread.start()
while input("") != "STOP":
    continue

sender.stop_stream()
