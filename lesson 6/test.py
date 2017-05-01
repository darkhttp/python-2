import  threading
import time

for i in range(10):
    a = threading.Thread(target = time.sleep, args = (5,))
    a.start()
