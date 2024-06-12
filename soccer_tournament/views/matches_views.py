from rest_framework import viewsets
from soccer_tournament.serializers.matches_serializer import MatchesSerializer
from soccer_tournament.models.matches import Matches

class MatchesView(viewsets.ModelViewSet):
    serializer_class = MatchesSerializer
    queryset = Matches.objects.all()