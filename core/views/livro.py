from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Livro
from core.serializers import LivroSerializer, LivroSerializer

...
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer