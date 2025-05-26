# lib/debug.py

from scripts.setup_db import setup_database
from lib.db.seed import seed_database
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def run_debug_tests():
    print("=== Setting up database ===")
    setup_database()

    print("\n=== Seeding database ===")
    conn = get_connection()
    seed_database(conn)

    print("\n=== Testing Author creation and lookup ===")
    author = Author.find_by_name("J.K. Rowling")
    if author:
        print(f"Found Author: {author.name} (ID: {author.id})")
    else:
        print("Author 'J.K. Rowling' not found.")

    print("\n=== Testing Magazine creation and lookup ===")
    magazine = Magazine.find_by_name("Fantasy Today")
    if magazine:
        print(f"Found Magazine: {magazine.name} (Category: {magazine.category}, ID: {magazine.id})")
    else:
        print("Magazine 'Fantasy Today' not found.")

    print("\n=== Testing Articles by Author ===")
    if author:
        articles = author.articles()
        if articles:
            for art in articles:
                print(f"- {art.title} in magazine ID {art.magazine_id}")
        else:
            print(f"No articles found for author {author.name}")

    print("\n=== Testing Authors who wrote for a Magazine ===")
    if magazine:
        articles = magazine.articles()
        authors = set()
        for art in articles:
            a = Author.find_by_id(art.author_id)
            if a:
                authors.add(a.name)
        if authors:
            print(f"Authors who wrote for {magazine.name}:")
            for name in authors:
                print(f"- {name}")
        else:
            print(f"No authors found for magazine {magazine.name}")

if __name__ == "__main__":
    try:
        run_debug_tests()
    except Exception as e:
        print(f"Error during debug tests: {e}")
