import threading
import time

"""Плохой способ реализации"""
counter_bad = 0

def bad():
    global counter_bad
    for i in range(10_000_000):
        counter_bad += 1

def race_demo_bad():
    global counter_bad
    counter_bad = 0

    threads = []
    for i in range(5):
        t = threading.Thread(target=bad)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

    print(f"резульат: {counter_bad} (должно быть 5_000_000)")

"""Хороший вариант реализации"""
counter_good = 0
lock = threading.Lock()

def good():
    global counter_good
    for i in range(10_000_000):
        with lock:
            counter_good += 1

def race_demo_good():
    global counter_good
    counter_good = 0
    threats = []
    for i in range(5):
        t = threading.Thread(target=good)
        t.start()
        threats.append(t)

    for t in threats:
        t.join()
    print(f"резульат: {counter_good} (должно быть 5_000_000)")

if __name__ == "__main__":
    race_demo_bad()
    race_demo_good()        