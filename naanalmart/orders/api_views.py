from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import authentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from orders.serializers import OrderSerializer
from orders.models import Orders
from rest_framework import status
from seller.models import Seller


class OrderCreateApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    #model = Orders
    serializer_class = OrderSerializer
    queryset =  Orders.objects.all()


    #def get_queryset(self):
    #   return Orders(seller_id=request.user.seller_id)


class OrderRetriveApiView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    model = Orders
    serializer_class = OrderSerializer
    


class OrderDestroyApiView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    model = Orders
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()



#return Response({'clients': ['You do not have permission.']},
 #                                   status=status.HTTP_400_BAD_REQUEST)

# def post(self, request, format=None):
#         """
#         POST method to add new employee user.
#         """

#         # Get request data
#         data = request.data

#         # Set organization to current user's organization
#         data['organization'] = request.user.organization.id

#         # Get list of clients
#         if request.data.get('clients', '') != '':
#             data['clients'] = [int(client) for client in request.data.get('clients', '').split(',')]

#         # Get list of permisssion
#         if request.data.get('user_permissions', '') != '':
#             data['user_permissions'] = [int(permissions) for permissions in request.data.get('user_permissions', '').split(',')]

#         # Serializer for validation and saving of data.
#         serialized = UserCreateUpdateSerializer(
#             data=data,
#             fields=[
#                 'first_name', 'last_name', 'email', 'is_active',
#                 'organization', 'designation', 'clients', 'password' , 'user_permissions'
#             ]
#         )

#         if serialized.is_valid():
#             # Check if this user has permission to assign provided clients.
#             clients = serialized.validated_data['clients']
#             serialized.validated_data['organization'] = request.user.organization
#             client_ids = [client.id for client in clients]
#             for client_id in client_ids:
#                 if not request.user.clients.filter(id=client_id).exists():
#                     return Response({'clients': ['You do not have permission to create user for this client.']},
#                                     status=status.HTTP_400_BAD_REQUEST)

#             # Check if this user has permissions
#             user_permissions = serialized.validated_data['user_permissions']
#             permission_ids = [user_permission.id for user_permission in user_permissions]
#             for permission_id in permission_ids:
#                 if not request.user.user_permissions.filter(id=permission_id).exists():
#                     return Response({'clients': ['You do not have permission.']},
#                                     status=status.HTTP_400_BAD_REQUEST)

#             # If everything is ok, then save.
#             user = serialized.save()

#             # Save password with inbuilt function.
#             user.set_password(user.password)
#             user.save()

#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

















    


    # def post(self, request, format=None):
    #     print request.user.email
    #     print request.user.seller_id
    #     data = Orders.objects.create(seller=request.user.seller_id)
    #     return Response(data, status=status.HTTP_200_OK)

    #     data = request.data
    #     return Response(data, status=status.HTTP_200_OK)
    # #     data = request.data
    # #     #sell = Seller.objects.filter(seller_id=data.get('seller'))
    # #     print request.user.seller_id
    # #     for ele in sell:
    # #         if request.user.email == ele.email:
    # #             return Response(data, status=status.HTTP_200_OK)
    # #         else:
    # #             return Response({'seller': ['OOPS! make sure you are logged in']},status=status.HTTP_400_BAD_REQUEST)

    # # def get_queryset(self, *args, **kwargs):
    # #     return Seller.objects.filter(seller_id = pk)