import threading
import time

def worker(name, iterations):
    
    for i in range(iterations):
        print(f"{name}: шаг {i}")

        for _ in range(10_000_000):
            _= 1 + 1

def graphics():
    t1 = threading.Thread(target=worker, args=("A", 5))
    t2 = threading.Thread(target=worker, args=("B", 5))

    print("Запускаем поток")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    graphics()