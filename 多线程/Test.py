import threading
import time

value = 0

gLock = threading.Lock()

def writer_():
    global value
    gLock.acquire()  # 加锁
    for i in range(1000000000):
        value += 1
    gLock.release()  # 释放锁
    print(value)


def main():
    threading.Thread(target=writer_).start()
    threading.Thread(target=writer_).start()


if __name__ == '__main__':
    main()
