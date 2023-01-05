from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from .views import GroupViewSet, PostViewSet, CommentViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]