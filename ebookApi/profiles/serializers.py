from rest_framework import serializers

from profiles.models import ProfileModel, ProfileStatus

class ProfileModelSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = ProfileModel
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProfileModel
        fields = ("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):
    '''Profile status serializer '''
    user_profile = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileStatus
        fields = "__all__"