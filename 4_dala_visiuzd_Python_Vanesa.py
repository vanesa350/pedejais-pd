'''
1. https://pro2025.azurewebsites.net/journals
2. https://pro2025.azurewebsites.net/journals?year=2000
3. https://pro2025.azurewebsites.net/books?year=2020&genre=Fantasy
'''
import requests
import json

BASE_URL = "https://pro2025.azurewebsites.net"

# 4.1. uzdevums
url = f"{BASE_URL}/books"
response = requests.get(url)

if response.status_code == 200:
    print("Pieprasījums veiksmīgs")
else:
    print(f"Kļūda, kods: {response.status_code}")

books = response.json()

# 4.2. uzdevums
print("\n--- Visas grāmatas ---")
for book in books:
    print(f'Grāmata "{book["name"]}" ({book["year_published"]}), {book["pages"]} lpp.')

# 4.3. uzdevums
titles = [book["name"] for book in books]
with open("nosaukumi.json", "w", encoding="utf-8") as f:
    json.dump(titles, f, ensure_ascii=False, indent=2)
print("\nGrāmatu nosaukumi saglabāti failā 'nosaukumi.json'")

# 4.4. uzdevums
oldest_book = min(books, key=lambda b: b["year_published"])
print(f"\nVisvecākā grāmata: {oldest_book['name']}")

# 4.5. uzdevums
total_pages = sum(int(book["pages"]) for book in books)
avg_price = sum(int(book["price"]) for book in books) / len(books)
print(f"\nKopējais lappušu skaits: {total_pages}")
print(f"Vidējā cena: {avg_price:.2f}")

# 4.6. uzdevums
def garakais_nosaukums(books):
    return max(books, key=lambda b: len(b["name"]))

book_long = garakais_nosaukums(books)
print(f"\nGrāmata ar garāko nosaukumu: autors - {book_long.get('author', 'Nav norādīts')}, gads - {book_long['year_published']}")

# 4.7. uzdevums
data_structure = []
for book in books:
    entry = {
        "name": book.get("name"),
        "year_published": book.get("year_published"),
        "pages": book.get("pages"),
        "price": book.get("price"),
        "genre": book.get("genre"),
        "author": book.get("author") if book.get("author") else "Nav norādīts"
    }
    data_structure.append(entry)

# 4.8. uzdevums
authors = sorted(
    set(b["author"] for b in data_structure if b["author"] != "Nav norādīts"),
    key=str.upper
)
print("\n--- Autori alfabēta secībā ---")
for author in authors:
    print(author)

# 4.9. uzdevums
from collections import Counter
author_counts = Counter(
    b["author"] for b in data_structure if b["author"] != "Nav norādīts"
)
top_author, top_count = author_counts.most_common(1)[0]
top_books = [b["name"] for b in data_structure if b["author"] == top_author]

print(f"\nAutors ar visvairāk grāmatu ({top_count}), - {top_author}:")
for i, title in enumerate(top_books, 1):
    print(f'{i}. "{title}"')

# 4.10. uzdevums
import random

journals_response = requests.get(f"{BASE_URL}/journals")
all_journals = journals_response.json()

random_journals = random.sample(all_journals, 10)
journal_list = [{"name": j["name"], "publisher": j["publisher"]} for j in random_journals]

def pievienot_zurnalu(lst, name, publisher):
    new_journal = {"name": name, "publisher": publisher}
    lst.insert(0, new_journal)
    return lst

def dzest_pedejo(lst):
    if lst:
        lst.pop()
    return lst