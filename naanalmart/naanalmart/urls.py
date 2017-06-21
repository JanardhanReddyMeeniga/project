from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),

    #api urls
    url(r'^api/sellers/', include('seller.urls')),
    url(r'^api/orders/', include('orders.urls')),
]



'''
(?P<pk>\d+)/$

{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImphbmFAZ21haWwuY
29tIiwidXNlcl9pZCI6MSwiZW1haWwiOiJqYW5hQGdtYWlsLmNvbSIsImV4cCI6MTQ5Nzg3NDU3Mn0.d
PBf3A-mJ-gjeNHTATKWVeO3E1xpzzJA-Wv9NALwqns"}

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImphbmFAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZW1haWwiOiJqYW5hQGdtYWlsLmNvbSIsImV4cCI6MTQ5Nzg3NDU3Mn0.dPBf3A-mJ-gjeNHTATKWVeO3E1xpzzJA-Wv9NALwqns" http://localhost:8000/protected-url/


curl -X POST -H "Content-Type: application/json" -d '{"email":"jana@gmail.com","password":"jana"}' http://localhost:8000/api-token-auth/

'''