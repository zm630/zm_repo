import time
import threading

def print_time():
      time.sleep(3)
      current_time = time.strftime("%H:%M:%S",time.localtime())
      print(current_time)
thread = threading.Thread(target=print_time)
thread.start()