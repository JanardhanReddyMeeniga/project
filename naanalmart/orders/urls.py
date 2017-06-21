from django.conf.urls import include, url
from django.contrib import admin
from orders.api_views import OrderCreateApiView
from orders.api_views import OrderRetriveApiView
from orders.api_views import OrderDestroyApiView

urlpatterns = [
    #api urls
    url(r'^list/', OrderCreateApiView.as_view()),
    url(r'^retrive/(?P<pk>\d+)/$', OrderRetriveApiView.as_view()),
    url(r'^destroy/(?P<pk>\d+)/$', OrderDestroyApiView.as_view()),
]
