from django.urls import path, include
from .api import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register('router', bookviewset, basename = "router")

urlpatterns = [
    path("", include(router.urls)),
]
