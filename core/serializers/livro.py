from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora, Livro
from core.serializers import (
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco")

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1