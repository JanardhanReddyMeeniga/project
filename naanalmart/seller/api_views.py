from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import authentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from seller.serializers import SellerSerializer
from seller.models import Seller
from seller.permissions import IsOwnerAndAuth

class SellerList(ListAPIView):

    #authentication_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated,)
    model = Seller
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()

