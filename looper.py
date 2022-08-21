import schedule
import time
import downloadchecker

def func():
    exec(open("downloadchecker.py").read())

schedule.every(1).minutes.do(func)
while True:
    schedule.run_pending()
    time.sleep(1)