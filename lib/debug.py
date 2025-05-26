import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.models.magazine import  Magazine
from lib.models.author import Author

from lib.models.article import Article

author = Author(name="Alice")
author.save()

magazine = Magazine(title="Health Weekly", issue=3)
magazine.save()

article = Article("5 Ways to Stay Fit", author.id, magazine.id)
article.save()

print(f"{article.title} published in {article.magazine().title} by {article.author().name}")
