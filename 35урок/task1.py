import multiprocessing
import threading
import time

def cpu_inti():
    counter = 0
    for i in range(50_000_000):
        counter += i ** 2
    return counter

def with_threading():
    start = time.time()
    threads = []

    for _ in range(4):
        t = threading.Thread(target=cpu_inti)
        t.start()
        threads.append(t)

    for t in threads:
        t.join
    print(f"Потоки {time.time() - start} секунд")

def with_processing():
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        res = pool.map(lambda _: cpu_inti(), range(4))
    print(f"Процессы: {time.time() - start:.2f} секунд")

if __name__ == "__main__":
    with_threading()
    with_processing()