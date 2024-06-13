from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

from soccer_tournament.serializers.matches_serializer import MatchesSerializer
from soccer_tournament.models.matches import Matches
from soccer_tournament.serializers.team_serializer import TeamSerializer
from soccer_tournament.models.team import Team

class MatchesView(viewsets.ModelViewSet):
    serializer_class = MatchesSerializer
    queryset = Matches.objects.all()

    def create(self, request):
        serializer = MatchesSerializer(data=request.data)
        if serializer.is_valid():
            if request.data['status'] == 'finished':
                team_one = Team.objects.get(id=request.data['team_one'])
                serializer_team_one = TeamSerializer(team_one)
                team_two = Team.objects.get(id=request.data['team_two'])
                serializer_team_two = TeamSerializer(team_two)
                
                team_one_data = {
                    **serializer_team_one.data,
                    'goals_favor': str(int(request.data['goals_team_one']) + int(serializer_team_one.data['goals_favor'])),
                    'goals_against': str(int(request.data['goals_team_two']) + int(serializer_team_one.data['goals_against'])),
                }

                team_two_data = {
                    **serializer_team_two.data,
                    'goals_favor': str(int(request.data['goals_team_two']) + int(serializer_team_two.data['goals_favor'])),
                    'goals_against': str(int(request.data['goals_team_one']) + int(serializer_team_two.data['goals_against'])),
                }
                
                if request.data['goals_team_one'] > request.data['goals_team_two']:
                    team_one_data['matches_won'] = str(int(team_one_data['matches_won']) + 1)
                    team_two_data['lost_matches'] = str(int(team_two_data['lost_matches']) + 1)
                elif request.data['goals_team_one'] < request.data['goals_team_two']:
                    team_two_data['matches_won'] = str(int(team_two_data['matches_won']) + 1)
                    team_one_data['lost_matches'] = str(int(team_one_data['lost_matches']) + 1)
                else:
                    team_one_data['tied_matches'] = str(int(team_one_data['tied_matches']) + 1)
                    team_two_data['tied_matches'] = str(int(team_two_data['tied_matches']) + 1)

                serializer_team_one_update = TeamSerializer(team_one, data=team_one_data)
                serializer_team_two_update = TeamSerializer(team_two, data=team_two_data)

                if serializer_team_one_update.is_valid() and serializer_team_two_update.is_valid():
                    serializer_team_one_update.save()
                    serializer_team_two_update.save()
                else:
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        matches = Matches.objects.get(id=pk)
        serializer = MatchesSerializer(matches, data=request.data)
        if serializer.is_valid():
            if request.data['status'] == 'finished':
                team_one = Team.objects.get(id=request.data['team_one'])
                serializer_team_one = TeamSerializer(team_one)
                team_two = Team.objects.get(id=request.data['team_two'])
                serializer_team_two = TeamSerializer(team_two)
                
                team_one_data = {
                    **serializer_team_one.data,
                    'goals_favor': str(int(request.data['goals_team_one']) + int(serializer_team_one.data['goals_favor'])),
                    'goals_against': str(int(request.data['goals_team_two']) + int(serializer_team_one.data['goals_against'])),
                }

                team_two_data = {
                    **serializer_team_two.data,
                    'goals_favor': str(int(request.data['goals_team_two']) + int(serializer_team_two.data['goals_favor'])),
                    'goals_against': str(int(request.data['goals_team_one']) + int(serializer_team_two.data['goals_against'])),
                }
                
                if request.data['goals_team_one'] > request.data['goals_team_two']:
                    team_one_data['matches_won'] = str(int(team_one_data['matches_won']) + 1)
                    team_two_data['lost_matches'] = str(int(team_two_data['lost_matches']) + 1)
                elif request.data['goals_team_one'] < request.data['goals_team_two']:
                    team_two_data['matches_won'] = str(int(team_two_data['matches_won']) + 1)
                    team_one_data['lost_matches'] = str(int(team_one_data['lost_matches']) + 1)
                else:
                    team_one_data['tied_matches'] = str(int(team_one_data['tied_matches']) + 1)
                    team_two_data['tied_matches'] = str(int(team_two_data['tied_matches']) + 1)

                serializer_team_one_update = TeamSerializer(team_one, data=team_one_data)
                serializer_team_two_update = TeamSerializer(team_two, data=team_two_data)

                if serializer_team_one_update.is_valid() and serializer_team_two_update.is_valid():
                    serializer_team_one_update.save()
                    serializer_team_two_update.save()
                else:
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)