from rest_framework.routers import DefaultRouter

from shortener.api.views import ShortUrls, TemplateViewSet

router = DefaultRouter()

router.register('shorter', ShortUrls, basename='Shorter')
router.register('templates', TemplateViewSet, basename='Templates')
