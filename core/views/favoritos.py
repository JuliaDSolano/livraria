from rest_framework import viewsets
from core.models import Favorito
from core.serializers import FavoritoSerializer
from rest_framework.permissions import IsAuthenticated

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




