#Логирование времени
from datetime import datetime
def logInfo(message):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] [INFO]{message}")
def errorInfo(message):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] [ERROR]{message}")