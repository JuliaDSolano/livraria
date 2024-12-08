from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Livro
from core.serializers import (
    LivroListRetrieveSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroListRetrieveSerializer
        return LivroSerializer
    
    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroRetrieveSerializer
        return LivroSerializer
    