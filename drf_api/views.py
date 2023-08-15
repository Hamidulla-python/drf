

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
#from .serializers import UserSerializer
from .models import Jobs


# class UserViewSet(viewsets.ModelViewSet):
#
#     queryset = Jobs.objects.all()
#     serializer_class = UserSerializer