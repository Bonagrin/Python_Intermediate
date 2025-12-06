from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    # kapcsolódó szerző
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)

    def __str__(self):
        # visszaadjuk a könyv nevét és a szerző nevét (ha elérhető)
        author_name = self.author.name if self.author else 'ismeretlen'
        return f"{self.name} ({self.isbn}) - {author_name}"
