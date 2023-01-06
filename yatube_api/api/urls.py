from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
