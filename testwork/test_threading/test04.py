import time
import threading

def print_time():
    while True:
      time.sleep(1)
      current_time = time.strftime("%H:%M:%S",time.localtime())
      print(current_time)
if __name__ == '__main__':
    # thread = threading.Timer(1.0,function=print_time)
    thread = threading.Thread(target=print_time)
    thread.start()