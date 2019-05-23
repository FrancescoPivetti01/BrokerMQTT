import threading
import Telegram
import MQTT

thread1 = threading.Thread(target=Telegram.main)
thread2 = threading.Thread(target=MQTT.main)
thread1.start()
thread2.start()
