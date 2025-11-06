from django.urls import path, include
from rest_framework import routers
from .api import *
router = routers.DefaultRouter()
router.register('router', bookviewset, basename="router")

urlpatterns = [
    path("", include(router.urls)),

    # user routes
    path("users/", getuserdets),
    path("users/add/", inputuserdata),
    path("users/<int:id>/delete/", deleteuserdata),
    path("users/<int:id>/update/", updateuserdata),

    # application routes
    path("applications/", getapplication),
    path("applications/add/", inputapplication),
    path("applications/<int:id>/delete/", delete_application),
    path("applications/<int:id>/update/", updateapplication),
]
