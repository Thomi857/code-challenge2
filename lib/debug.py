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
    print(f"Found Author: {author.name} (ID: {author.id})")

    print("\n=== Testing Magazine creation and lookup ===")
    mag = Magazine.find_by_name("Fantasy Today")
    print(f"Found Magazine: {mag.name} - Category: {mag.category} (ID: {mag.id})")

    print("\n=== Testing Article creation and lookup ===")
    articles = Article.find_by_author(author.id)
    print(f"Articles by {author.name}:")
    for article in articles:
        print(f"- {article.title} (Magazine ID: {article.magazine_id})")

    print("\n=== Testing Author.magazines() method ===")
    mags = author.magazines()
    for m in mags:
        print(f"- {m.name} ({m.category})")

    print("\n=== Testing Magazine.authors() method ===")
    authors = mag.authors()
    for a in authors:
        print(f"- {a.name}")

    print("\n=== Testing Magazine.article_counts() class method ===")
    counts = Magazine.article_counts()
    for mag, count in counts:
        print(f"{mag.name} has {count} articles")

    print("\n=== Testing Author.top_author() class method ===")
    top_author = Author.top_author()
    print(f"Top author is {top_author.name}")

    print("\n=== Testing Article.delete() ===")
    if articles:
        print(f"Deleting article: {articles[0].title}")
        articles[0].delete()
        print("Deleted. Verifying deletion...")
        check = Article.find_by_id(articles[0].id)
        print(f"Article found? {'Yes' if check else 'No'}")

    print("\nAll tests completed.")


if __name__ == "__main__":
    run_debug_tests()
