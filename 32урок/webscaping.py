'''
h3 - заголовок величины 3
a - ссылка
p - абзац
ol - нумерованный список
ul - ненумерованный(маркированный) список
li - строчка списка
'''
import requests
from bs4 import BeautifulSoup
import csv

page = 1
book_data = []

while True:
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')
    
    if not books:
        print("Книги не найдены.")
        break

    for book in books:
        try:
            name = book.find('h3').find('a')['title']
        except:
            name = "Ошибка: нет названия"
        
        try:
            price = book.find('p', class_='price_color').text.strip()
        except:
            price = "Ошибка: нет цены"
        
        book_data.append([name, price])

    print(f"Страница {page}: {len(books)} книг")
    page += 1

    if page == 10:
        break
with open('books4.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Название', 'Цена'])
    writer.writerows(book_data)

print(f"Сохранено {len(book_data)} названий книг")

print("\nСтатистика")
print(f"Всего книг: {len(book_data)}")

prices = [book[1] for book in book_data if book[1] > 0]

if price:
    avg_price = sum(book_data)/len(book_data)
    max_price = max(book_data)
    min_price = min(book_data)
