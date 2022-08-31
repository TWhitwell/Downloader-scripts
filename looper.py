import schedule
import time
import sys


def func():
    file = open('failedcounter.txt', 'r')
    n = int(file.read())
    if n <= 6:
        exec(open("downloadchecker.py").read())
    else:
        subject = 'Script has failed 6 times'
        plain = 'To prevent spamming it has been disabled'
        html = '<b> To prevent spamming it has been disabled </b>'
        exec(open("emailer.py").read())
        print("failed")
        schedule.clear()
        file = open('failedcounter.txt', 'w')
        file.write('0')
        file.close()
        n = 1
        exit()

schedule.every(1).minutes.do(func)
    while True:
        schedule.run_pending()
        time.sleep(1)