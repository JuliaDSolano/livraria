from django.conf import settings
from django.db import models

class Favorito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livro = models.ForeignKey('Livro', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'livro')

    def __str__(self):
        return f"{self.user.username} favorited {self.book.title}"
    
