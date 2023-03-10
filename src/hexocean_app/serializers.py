from rest_framework import serializers
from .models import User, Image, ImageArray, Tier, Size


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
            "email",
            "firstname",
            "lastname",
            "tier",
            "password",
        )
        model = User

    def create(self, validated_data):
        user = User(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'image_array',
        )
        model = Image


class ImageArraySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    image = serializers.ImageField(write_only=True)

    class Meta:
        fields = (
            "id",
            "title",
            "images",
            "user",
            "image",
        )
        model = ImageArray


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "height",
        )
        model = Size


class TierSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)

    class Meta:
        fields = (
            "id",
            "name",
            "sizes",
            "expired_link",
            "full_size",
        )
        model = Tier
