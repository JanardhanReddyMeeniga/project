from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from seller.api_views import SellerList
urlpatterns = [

    url(r'^auth/', SellerList.as_view()),
]
