from rest_framework import serializers
from api.models import Users, Followers

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
        fields = ('id', 'username', 'email', 'password', 'birthday', 'company', 'location')              

class FollowSerializer(serializers.ModelSerializer):
    """
    Serializing Followers
    """
    class Meta:
        model = Followers
        fields = ('id', 'user_id.id', 'followed_by_id.id', 'followed_at') 
