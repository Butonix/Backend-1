from rest_framework import serializers

from accounts.serializers.user import UserWithProfileSerializer
from multimedia.models import (Multimedia, MultimediaAudio, MultimediaImage,
                               MultimediaVideo, MultimediaVideoUrl)
from utils.helper import get_youtube_video_data


class MultimediaVideoUrlDetailSerializer(serializers.ModelSerializer):
    yt_info = serializers.SerializerMethodField()

    @staticmethod
    def get_yt_info(obj):
        return get_youtube_video_data(obj.video_url)

    class Meta:
        model = MultimediaVideoUrl
        fields = ["id", "yt_info", "video_url"]


class MultimediaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaVideo
        fields = "__all__"


class MultimediaAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaAudio
        fields = "__all__"


class MultimediaVideoUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaVideoUrl
        fields = "__all__"


class MultimediaImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = MultimediaImage
        fields = "__all__"


class MultimediaPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = "__all__"
        read_only_fields = ("is_approved",)

    def create(self, validated_data):
        validated_data["uploaded_by"] = self.context["request"].user
        branch = Multimedia.objects.create(**validated_data)
        return branch


class MultimediaSerializer(serializers.ModelSerializer):
    multimedia_images = MultimediaImageSerializer(many=True, read_only=True)
    multimedia_videos = MultimediaVideoSerializer(many=True, read_only=True)
    multimedia_video_urls = MultimediaVideoUrlsSerializer(many=True, read_only=True)
    multimedia_audios = MultimediaAudioSerializer(many=True, read_only=True)

    uploaded_by = UserWithProfileSerializer()

    class Meta:
        model = Multimedia
        fields = "__all__"
        depth = 1
