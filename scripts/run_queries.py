from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Create authors and save to DB
author1 = Author.find_by_name("Alice Walker") or Author("Alice Walker")
author1.save()

author2 = Author.find_by_name("George Orwell") or Author("George Orwell")
author2.save()

# Create magazines and save
mag1 = Magazine.find_by_name("Science Weekly") or Magazine("Science Weekly", "Science")
mag1.save()

mag2 = Magazine.find_by_name("Literary Digest") or Magazine("Literary Digest", "Literature")
mag2.save()

# Create articles by calling add_article on authors (links to magazines)
article1 = author1.add_article(mag1, "The Nature of Things")
article2 = author2.add_article(mag2, "Fiction and Reality")
article3 = author1.add_article(mag1, "Future of Tech")

# Query magazines written by author1
print(f"Magazines written by {author1.name}:")
for mag in author1.magazines():
    print(f"- {mag.name}")

# Query authors who wrote for mag1
print(f"Authors who wrote for {mag1.name}:")
for article in mag1.articles():
    # article.author_id links to author
    author = Author.find_by_id(article.author_id)
    print(f"- {author.name}")
