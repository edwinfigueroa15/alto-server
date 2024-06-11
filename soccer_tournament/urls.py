from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from soccer_tournament import views

router = routers.DefaultRouter()
router.register('team', views.TeamView, basename='team')
router.register('matches', views.MatchesView, basename='matches')

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title='Soccer Tournament API')),
]