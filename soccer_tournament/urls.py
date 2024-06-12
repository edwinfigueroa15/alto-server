from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from soccer_tournament.views.team_views import TeamView
from soccer_tournament.views.matches_views import MatchesView

router = routers.DefaultRouter()
router.register('team', TeamView, basename='team')
router.register('matches', MatchesView, basename='matches')

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title='Soccer Tournament API')),
]