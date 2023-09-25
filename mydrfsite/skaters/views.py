from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from skaters.models import Skaters
from skaters.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from skaters.serializers import SkatersSerializer


class SkatersAPIList(generics.ListCreateAPIView):
    queryset = Skaters.objects.all()
    serializer_class = SkatersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SkatersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Skaters.objects.all()
    serializer_class = SkatersSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class SkatersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Skaters.objects.all()
    serializer_class = SkatersSerializer
    permission_classes = (IsAdminOrReadOnly,)

