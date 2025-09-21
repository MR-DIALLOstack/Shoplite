from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from .permissions import IsSuperUserOrReadOnly


class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrReadOnly]

