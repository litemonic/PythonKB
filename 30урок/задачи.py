import requests

url = "https://uselessfacts.jsph.pl/random.json?language=ru"

def GetRandomText():
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            fact = data

            print(fact)
        else:
            print(f"Ошибка: Сервер вернул код {response.status_code}")

    except requests.exceptions.Timeout:
        print("Превышено время ожидания")
    except requests.exceptions.ConnectionError:
        print("Нет соеденения с сервером")
    except Exception as e:
        print(f"Произошла ошлибка: {e}")
if __name__ == "__main__":
    GetRandomText()