# scrap_books.py
import os
import mysql.connector
from dotenv import load_dotenv
from scraper import scrape_page

load_dotenv()

# Connexion à la base de données
db = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PWD"),
    database=os.getenv("DB")
)
cursor = db.cursor()

def main():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    for page in range(1, 51):  # Refactor with dynamic scrapping
        scrape_page(base_url.format(page), cursor, db)
        
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
