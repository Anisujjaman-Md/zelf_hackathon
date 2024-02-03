from django.urls import path, include
from rest_framework import routers
from zelf.views import ContentListView, AggregatedStatsView

router = routers.DefaultRouter()
router.register('content-list', ContentListView, basename='content-list')
router.register('statistics', AggregatedStatsView, basename='statistics')
urlpatterns = [
    path('zelf/', include(router.urls)),
]
