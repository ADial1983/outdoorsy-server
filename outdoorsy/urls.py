"""outdoorsy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from outdoorsyapi.views import register_user, login_user
from outdoorsyapi.views import TrailView, ImageView, TrailImageView, ReviewView, RatingView, RatingReviewView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'trails', TrailView, 'trail')
router.register(r'images', ImageView, 'image')
router.register(r'trailimages', TrailImageView, 'trailimage')
router.register(r'reviews', ReviewView, 'review')
router.register(r'ratings', RatingView, 'rating')
router.register(r'ratingreviews', RatingReviewView, 'ratingreview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
