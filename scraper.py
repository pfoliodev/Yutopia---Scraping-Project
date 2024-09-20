# scraper.py
import requests
from bs4 import BeautifulSoup
from utils import string_to_boolean, convert_string_to_int, convert_string_to_float

def scrape_page(url, cursor, db):
    response_all_book = requests.get(url)
    soup = BeautifulSoup(response_all_book.content, 'html.parser')

    for book in soup.select('article.product_pod'):
        # Scraping book
        title_element = book.h3.a
        title = title_element.get('title', 'Titre non disponible') if title_element else 'Titre non disponible'

        price_element = book.select_one('p.price_color')
        price = price_element.text if price_element else 'Prix non disponible'

        rating_element = book.select_one('p.star-rating')
        rating = len(rating_element['class'][1]) if rating_element and len(rating_element['class']) > 1 else 'Évaluation non disponible'

        stock_element = book.select_one('p.availability')
        stock = string_to_boolean(stock_element) if stock_element else False

        book_url_element = book.h3.a
        book_url = book_url_element.get('href', 'URL non disponible') if book_url_element else 'URL non disponible'

        img_src = soup.find('img')['src']
        cleaned_img_path = img_src.replace('../../', '')

        # Category
        book_page_url = f"https://books.toscrape.com/catalogue/{book_url}"
        response = requests.get(book_page_url)
        book_detail = BeautifulSoup(response.content, 'html.parser')
        breadcrumb_li = book_detail.find('ul', class_="breadcrumb").find_all('li')[2].getText()

        # Number of product available
        availability_p = book_detail.find("p", class_="instock").text
        availability_left = convert_string_to_int(availability_p)

        # Insert data in db
        insert_book(cursor, db, title, price, rating, stock, availability_left, cleaned_img_path, breadcrumb_li)

def insert_book(cursor, db, title, price, rating, stock, availability_left, cleaned_img_path, breadcrumb_li):
    cursor.execute("""
        INSERT INTO book (title, price, rating, in_stock, nb_availlable, img, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (title, price, rating, stock, availability_left, cleaned_img_path, breadcrumb_li))
    db.commit()
