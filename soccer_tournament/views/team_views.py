from rest_framework import viewsets
from soccer_tournament.serializers.team_serializer import TeamSerializer
from soccer_tournament.models.team import Team

class TeamView(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()