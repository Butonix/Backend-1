from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from article.serializers.action import CommentPostSerializer, CommentSerializer
from article.sub_models.action import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    filterset_fields = ["article", "writer"]

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create"]:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return CommentPostSerializer
        else:
            return CommentSerializer
