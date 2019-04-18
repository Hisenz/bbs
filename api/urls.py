from django.urls import path, include
from api.views import postview, rankview, recommended, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', postview.PostSet)
router.register(r'ranks', rankview.RankSet)
router.register(r'recommended', recommended.RecommendedSet)
router.register(r'ReviewPosts', postview.PostSetOrderForReview)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]