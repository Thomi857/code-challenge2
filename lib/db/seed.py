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
            Author("J.K. Rowling"),
            Author("Stephen King"),
            Author("George R.R. Martin"),
            Author("Agatha Christie"),
            Author("Ernest Hemingway")
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
            Article("The Magic of World Building", authors[0].id, magazines[0].id),
            Article("From Rags to Riches: My Writing Journey", authors[0].id, magazines[4].id),
            Article("Why We Love to Be Scared", authors[1].id, magazines[1].id),
            Article("Writing Every Day: A Discipline", authors[1].id, magazines[4].id),
            Article("Complex Characters in Fantasy", authors[2].id, magazines[0].id),
            Article("When Will Winds of Winter Come Out?", authors[2].id, magazines[0].id),
            Article("The Perfect Murder Mystery", authors[3].id, magazines[2].id),
            Article("Poirot's Greatest Cases", authors[3].id, magazines[2].id),
            Article("The Old Man and the Sea: Reflections", authors[4].id, magazines[3].id),
            Article("Writing War Stories", authors[4].id, magazines[4].id)
        ]
        for article in articles:
            article.save()

        conn.commit()
        print("Database seeded successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding database: {e}")