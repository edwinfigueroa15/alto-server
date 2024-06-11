from rest_framework import viewsets
from soccer_tournament.serializer import TeamSerializer, MatchesSerializer
from soccer_tournament.models import Team, Matches

# Create your views here.
class TeamView(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class MatchesView(viewsets.ModelViewSet):
    serializer_class = MatchesSerializer
    queryset = Matches.objects.all()