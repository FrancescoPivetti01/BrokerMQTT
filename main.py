import threading
import Telegram
import MQTT

thread1 = threading.Thread(target=Telegram.test)
thread2 = threading.Thread(target=MQTT.test)
thread1.start()
thread2.start()
