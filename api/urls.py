from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import PostView, CommentView, GroupView, FollowView


router = DefaultRouter()
router.register('posts', PostView, basename='posts')

router.register('group', GroupView, basename='group')

router.register('follow', FollowView, basename='follow')


comments_router = routers.NestedSimpleRouter(router, r'posts', lookup='posts')
comments_router.register(r'comments', CommentView, basename='comments')




urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),

]

urlpatterns += [
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]