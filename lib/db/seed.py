from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine
from sqlite3 import Connection   

def seed_database(conn: Connection):
    try:
        cursor = conn.cursor()

        # Clear existing data
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()

        # Create authors
        authors = [
            Author("J.K. Rowling", "jk@example.com"),
            Author("Stephen King", "sk@example.com"),
            Author("George R.R. Martin", "grrm@example.com"),
            Author("Agatha Christie", "ac@example.com"),
            Author("Ernest Hemingway", "eh@example.com")
        ]
        for author in authors:
            author.save()

        # Create magazines
        magazines = [
            Magazine("Fantasy Today", "Fantasy"),
            Magazine("Horror Monthly", "Horror"),
            Magazine("Mystery Digest", "Mystery"),
            Magazine("Literary Review", "Literature"),
            Magazine("Popular Fiction", "General")
        ]
        for magazine in magazines:
            magazine.save()

        # Create articles
        articles = [
            Article(authors[0], magazines[0], "The Magic of World Building"),
            Article(authors[0], magazines[4], "From Rags to Riches: My Writing Journey"),
            Article(authors[1], magazines[1], "Why We Love to Be Scared"),
            Article(authors[1], magazines[4], "Writing Every Day: A Discipline"),
            Article(authors[2], magazines[0], "Complex Characters in Fantasy"),
            Article(authors[2], magazines[0], "When Will Winds of Winter Come Out?"),
            Article(authors[3], magazines[2], "The Perfect Murder Mystery"),
            Article(authors[3], magazines[2], "Poirot's Greatest Cases"),
            Article(authors[4], magazines[3], "The Old Man and the Sea: Reflections"),
            Article(authors[4], magazines[4], "Writing War Stories")
        ]
        for article in articles:
            article.save()

        conn.commit()
        print("Database seeded successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding database: {e}")