from django.contrib.auth.models import User
from .models import Product, Retailer
from rest_framework import viewsets
from rest_framework import permissions
from Retailers.serializers import ProductSerializer, RetailerSerializer,UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = self.queryset
        username = self.request.query_params.get("username")
        email = self.request.query_params.get("email")
        if username:
            qs = qs.filter(username__icontains=username)
        if email:
            qs = qs.filter(email__icontains=email)
        return qs


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = self.queryset
        retailer_id = self.request.query_params.get("retailer_id")

        if retailer_id:
            qs = qs.filter(retailer_id=retailer_id)
        
        return qs


class RetailerViewSet(viewsets.ModelViewSet):
    queryset=Retailer.objects.all()
    serializer_class=RetailerSerializer
    permission_classes = [permissions.AllowAny]
