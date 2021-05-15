from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter

from multimedia.views import views
from multimedia.views.article import *
from multimedia.views.media_detail import *
from multimedia.views.multimedia import *
from multimedia.views.post_actions import (
    ArticleExtraStatus, CreateOrToggleBookmarkStatusOfArticle,
    CreateOrToggleBookmarkStatusOfMultimedia,
    CreateOrToggleLoveStatusOfArticle, CreateOrToggleLoveStatusOfMultimedia,
    CreateOrTogglePinStatusOfArticle, CreateOrTogglePinStatusOfMultimedia,
    ListArticleComments, ListMultimediaComments, MultimediaExtraStatus,
    PostComment)
from multimedia.views.post_list import (ListBookmarkedMediaView,
                                        ListLovedMediaView,
                                        ListPinnedMediaView)

router = DefaultRouter()
router.register(r"multimedia", views.MultimediaViewSet, basename="multimedia")
router.register(r"article", views.ArticleViewSet, basename="article")
urlpatterns = router.urls
urlpatterns += [
    path("create-article", CreateArticleWithImageList.as_view()),
    path("create-multimedia", CreateMultimediaWithMultimediaList.as_view()),
    path("article/<int:pk>/image", ListArticleImages.as_view()),
    path("multimedia/<int:pk>/video", ListMultimediaVideos.as_view()),
    path("multimedia/<int:pk>/audio", ListMultimediaAudios.as_view()),
    path("multimedia/<int:pk>/image", ListMultimediaImages.as_view()),
    path("multimedia/<int:pk>/video-url", ListMultimediaVideoUrls.as_view()),
    path("article-image/<int:pk>", ArticleImageDetailView.as_view()),
    path("multimedia-image/<int:pk>", MultimediaImageDetailView.as_view()),
    path("multimedia-audio/<int:pk>", MultimediaAudioDetailView.as_view()),
    path("multimedia-video/<int:pk>", MultimediaVideoDetailView.as_view()),
    path("multimedia/<int:pk>/toggle-approval", ToggleMultimediaApprovalView.as_view()),
    path("article/<int:pk>/toggle-approval", ToggleArticleApprovalView.as_view()),
    path("article/<int:pk>/toggle-love", CreateOrToggleLoveStatusOfArticle.as_view()),
    path(
        "article/<int:pk>/toggle-bookmark",
        CreateOrToggleBookmarkStatusOfArticle.as_view(),
    ),
    path(
        "article/<int:pk>/toggle-pin-status",
        CreateOrTogglePinStatusOfArticle.as_view(),
    ),
    path("article-extra-status/<int:pk>", ArticleExtraStatus.as_view()),
    path(
        "multimedia/<int:pk>/toggle-love",
        CreateOrToggleLoveStatusOfMultimedia.as_view(),
    ),
    path(
        "multimedia/<int:pk>/toggle-bookmark",
        CreateOrToggleBookmarkStatusOfMultimedia.as_view(),
    ),
    path(
        "multimedia/<int:pk>/toggle-pin-status",
        CreateOrTogglePinStatusOfMultimedia.as_view(),
    ),
    path("multimedia-extra-status/<int:pk>", MultimediaExtraStatus.as_view()),
    path("multimedia/<int:pk>/comment", ListMultimediaComments.as_view()),
    path("article/<int:pk>/comment", ListArticleComments.as_view()),
    path("comment", PostComment.as_view()),
    path("loved-media", ListLovedMediaView.as_view()),
    path("bookmarked-media", ListBookmarkedMediaView.as_view()),
    path("pinned-media", ListPinnedMediaView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
