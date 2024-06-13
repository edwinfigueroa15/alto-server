from rest_framework.serializers import ModelSerializer
from soccer_tournament.models.matches import Matches
from .team_serializer import TeamSerializer

class MatchesSerializer(ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['team_one'] = TeamSerializer(instance.team_one).data
        response['team_two'] = TeamSerializer(instance.team_two).data
        return response