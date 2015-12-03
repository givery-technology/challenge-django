from rest_framework import serializers
from api.models import Users

class UserSerializer(serializers.ModelSerializer):
    """
    Serializing all the Users
    """
    class Meta:
        model = Users
        fields = ('id', 'username', 'email')  
        
class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializing all the Users
    """
    class Meta:
        model = Users
        fields = ('email', 'password')              
