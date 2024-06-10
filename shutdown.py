import os
import time
from datetime import datetime

shutdown_hour = 15
shutdown_minute = 2


def shutdown_at_specified_time(hour, minute):
    while True:       
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
       
        if current_hour == hour and current_minute == minute:
            os.system("shutdown /s /t 1")  # Komenda wyłączenia dla Windows
            break

        time.sleep(60)

shutdown_at_specified_time(shutdown_hour, shutdown_minute)
