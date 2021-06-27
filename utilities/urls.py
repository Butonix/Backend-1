from rest_framework.routers import DefaultRouter

from utilities.views import (
    AboutUsImageViewSet, AboutUsViewSet,
    ServiceViewSet, ShowcaseGalleryViewSet,
    SliderImageViewSet, ServiceImageViewSet, FeedbackViewSet, FeedbackFileViewSet
)

router = DefaultRouter()
router.register(r"slider-image", SliderImageViewSet, basename="slider-image")
router.register(
    r"showcase-gallery", ShowcaseGalleryViewSet, basename="showcase-gallery"
)
router.register(r"service", ServiceViewSet, basename="service")
router.register(r"service-image", ServiceImageViewSet, basename="service-image")
router.register(r"about-us", AboutUsViewSet, basename="about-us")
router.register(r"about-us-image", AboutUsImageViewSet, basename="about-us-image")
router.register(r"feedback", FeedbackViewSet, basename="feedback")
router.register(r"feedback-file", FeedbackFileViewSet, basename="feedback-file")

urlpatterns = router.urls
