from rest_framework import serializers
from django.contrib.auth.models import User

class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']
        
        extra_kwargs = {
            'username'   : {'required': True, 'allow_blank': False},
            'first_name': {'required': True, 'allow_blank': False},
            'last_name' : {'required': True, 'allow_blank': False},
            'password'  : {'write_only': True, 'min_length': 8},
            'email'     : {'required': True, 'allow_blank': False}
        }
        
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']
        
        extra_kwargs = {
            'password'  : {'write_only': True, 'min_length': 8},
         }