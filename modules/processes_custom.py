from multiprocessing import Process
import os
import time
# TODO read more about Processing


def square():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()

for i in range(num_processes):
    p = Process(target=square)
    processes.append(p)

for j in processes:
    j.start()

for k in processes:
    k.join()


