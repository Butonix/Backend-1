from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from multimedia.models import Image, Multimedia, Sound, Video
from multimedia.serializers.list import MultimediaWithMediaListSerializer
from multimedia.serializers.multimedia import (MultimediaPOSTSerializer,
                                               MultimediaSerializer)
from multimedia.sub_models.media import VideoUrl
from utils.helper import get_youtube_video_data


class MultimediaViewSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer
    filterset_fields = ["is_approved", "type"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return MultimediaPOSTSerializer
        return super(MultimediaViewSet, self).get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        multimedia = self.get_object()
        multimedia_images = Image.objects.filter(multimedia=multimedia)
        multimedia_audios = Sound.objects.filter(multimedia=multimedia)
        multimedia_videos = Video.objects.filter(multimedia=multimedia)
        [image.image.delete() for image in multimedia_images]
        [audio.delete() for audio in multimedia_audios]
        [video.delete() for video in multimedia_videos]
        multimedia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MultimediaWithMediaListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = MultimediaWithMediaListSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            title = validated_data.get("title")
            description = validated_data.get("description")
            videos = validated_data.get("video")
            video_urls = validated_data.get("video_url")
            sounds = validated_data.get("sound")
            images = validated_data.get("image")
            multimedia = Multimedia.objects.create(
                title=title,
                description=description,
                uploaded_by=user,
            )
            if videos:
                for video in videos:
                    Video.objects.create(
                        video=video,
                        multimedia=multimedia,
                    )

            if video_urls:
                for video_url in video_urls:
                    yt_info = get_youtube_video_data(video_url)
                    VideoUrl.objects.create(
                        video_url=video_url, multimedia=multimedia, yt_info=yt_info
                    )

            if sounds:
                for sound in sounds:
                    Sound.objects.create(
                        sound=sound,
                        multimedia=multimedia,
                    )

            if images:
                for image in images:
                    Image.objects.create(
                        image=image,
                        multimedia=multimedia,
                    )
            return Response(
                MultimediaSerializer(multimedia).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
