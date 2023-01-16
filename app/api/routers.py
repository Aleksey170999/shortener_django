from rest_framework.routers import DefaultRouter

from app.api.views import ShortUrls, TemplateViewSet, FileViewSet

router = DefaultRouter()

router.register('shorter', ShortUrls, basename='Shorter')
router.register('templates', TemplateViewSet, basename='Templates')
router.register('excel', FileViewSet, basename='File')
