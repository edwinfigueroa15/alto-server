from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    position = models.CharField(max_length=2)
    points = models.CharField(max_length=3)
    matches_won = models.CharField(max_length=2)
    lost_matches = models.CharField(max_length=2)
    tied_matches = models.CharField(max_length=2)
    goals_favor = models.CharField(max_length=2)
    goals_against = models.CharField(max_length=2)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['position']

class Matches(models.Model):
    team_one = models.ForeignKey(Team, related_name='team_one', on_delete=models.CASCADE, null=False)
    team_two = models.ForeignKey(Team, related_name='team_two', on_delete=models.CASCADE, null=False)
    goals_team_one = models.CharField(max_length=2)
    goals_team_two = models.CharField(max_length=2)
    status = models.CharField(max_length=30)
    data_start = models.DateField(null=False)
    created = models.DateField(auto_now_add=True)