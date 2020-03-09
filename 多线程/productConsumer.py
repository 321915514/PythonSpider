# 生产者消费者

import threading
import time
import random

gTimes = 0
gTotalTimes = 10
gMoney = 1000

gCondition = threading.Condition()


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            if gTimes > gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            gCondition.notify_all()
            gTimes += 1
            print('%s生产了%d的钱,还剩%d的钱' % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print('%s准备消费%d,还剩%d的钱,钱不足' % (threading.current_thread(), money, gMoney))
                gCondition.wait()
            gMoney -= money
            print('%s消费了%d的钱,还剩%d的钱' % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        Consumer(name='消费者%d' % x).start()
    for x in range(5):
        Producer(name='生产者%d' % x).start()


if __name__ == '__main__':
    main()
