from rest_framework.serializers import ModelSerializer
from ecom.models import User, ShippingAddress
from ecom.serializer import ShippingAddressSerializer

class UserSerializer(ModelSerializer):
    shipping_address=ShippingAddressSerializer(many=True, read_only=True)
    # default_shipping_address = ShippingAddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = "__all__"

class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"

class CreateShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ["street", "city", "state", "zip_code", "country"]

