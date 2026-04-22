import multiprocessing
import time

def square(numbers):
    res = []
    for num in numbers:
        res.append(num**2)
    return res

def run_single():
    data = list(range(10_000_000))
    start = time.time()
    res = square(data)
    print(f"Без параллелизации {time.time() - start} секунд")

def run_multi():
    data = list(range(10_000_000))
    chunk_size = len(data) // 4
    chunk = [
        data[:chunk_size],
        data[chunk_size:2 * chunk_size],
        data[2*chunk_size:3*chunk_size],
        data[3*chunk_size:]
    ]
    start = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, chunk)

        final_res = []
        for t in results:
            final_res.extend(t)
        print(f"С параллелизацией {time.time() - start} секунд.")

if __name__ == "__main__":
    run_single()
    run_multi()