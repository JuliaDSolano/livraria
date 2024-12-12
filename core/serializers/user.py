from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import User
from uploader.models import Image
from uploader.serializers import ImageSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1