from rest_framework import serializers

from .models import Image, ImageArray, Size, Tier, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
            "tier",
            "password",
        )
        model = User

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "content",
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
