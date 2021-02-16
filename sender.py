from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('192.168.1.11',9999)
sender_thread = threading.Thread(target=sender.start_stream)

sender_thread.start()
while input("") != "STOP":
    continue

sender.stop_stream()
