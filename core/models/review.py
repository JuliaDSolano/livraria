from django.conf import settings
from django.db import models

class Review(models.Model):
    livro = models.ForeignKey('Livro', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} reviewed {self.book.title}"
