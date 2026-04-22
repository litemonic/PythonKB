import threading
import time

def count_operation():
    count = 0
    for i in range(50_000_000):
        count += 1

def run_single_thread():
    start = time.time()
    count_operation()
    print(f" Один поток: {time.time() - start} секунд")

def run_multi_thread():
    start = time.time()

    t1 = threading.Thread(target=count_operation)
    t2 = threading.Thread(target=count_operation)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Два потока: {time.time() - start} секунд")

if __name__ == "__main__":
    run_single_thread()
    run_multi_thread()