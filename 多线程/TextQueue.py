from queue import Queue
import time
import threading


def get_put(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)


def get_get(q):
    while True:
        print(q.get())


def main():
    q = Queue(5)
    threading.Thread(target=get_put, args=[q]).start()
    threading.Thread(target=get_get, args=[q]).start()


if __name__ == '__main__':
    main()