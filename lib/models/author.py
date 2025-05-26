import sqlite3
from lib.db.connection import get_connection  # Assume you have this helper

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name.strip()
        if not self.name:
            raise ValueError("Author name cannot be empty")

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?)", (self.name,)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id)
            )
        conn.commit()

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM authors WHERE name = ?", (name.strip(),))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(row[1], row[2], row[3], row[0]) for row in rows]
    
    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.id, m.name, m.category
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        return [Magazine(row[1], row[2], row[0]) for row in rows]
    

    @classmethod
    def top_author(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT au.id, au.name, COUNT(a.id) AS article_count
            FROM authors au
            JOIN articles a ON au.id = a.author_id
            GROUP BY au.id
            ORDER BY article_count DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None


    # ... existing __init__, save, find methods ...

    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.id, m.name, m.category
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        return [Magazine(row[1], row[2], row[0]) for row in rows]

    def add_article(self, magazine, title):
        from lib.models.article import Article
        from lib.models.magazine import Magazine
        if not isinstance(magazine, (Magazine,)):
            raise ValueError("Expected a Magazine instance")
        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        return [row[0] for row in rows]
