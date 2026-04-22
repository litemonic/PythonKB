import threading
import time
import requests

def utl(url):
    print(f"Начать загрузку {url}")
    response = requests.get(url)
    print(f"Закончили загрузку {url}, длина: {len(response.text)}")

def run_single():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]

    start = time.time()
    for url in urls:
        utl(url)
    print(f"Один поток: {time.time() - start:.2f} секунд")

def run_multi():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]
    start = time.time()
    threats = []
    for url in urls:
        t = threading.Thread(target=utl, args=(url,))
        t.start
        threats.append(t)

    for t in threats:
        t.join()
    print(f"Многопоточный: {time.time() - start:.2f} секунд")
    
if __name__ == "__main__":
    run_single()
    run_multi()