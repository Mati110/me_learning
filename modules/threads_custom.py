from threading import Thread
import time
# TODO read more about threading

db_value = 0


def square():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    threads = []
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=square)
        threads.append(t)

    for j in threads:
        j.start()

    for k in threads:
        k.join()

    print("end main")
