from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[ validators.UniqueValidator(queryset=User.objects.all()) ]
    )

    first_name = serializers.CharField(
        required=True,
        max_length=30,
    )

    last_name = serializers.CharField(
        required=True,
        max_length=30,
    )

    password = serializers.CharField(
        write_only=True,
        validators=[ validate_password ],
        style={'input_type': 'password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        validators=[ validate_password ],
        style={'input_type': 'password'},
        required=True
    )
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        )
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Password did not match'})
        return data


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'is_staff'
        )
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CustomTokenSerializer(TokenSerializer):
    user = RegisterSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')