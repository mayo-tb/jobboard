from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics, permissions
from .models import Application
from .api import Applicationserializer

class ApplyJobView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = Applicationserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
