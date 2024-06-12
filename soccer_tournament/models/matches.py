from django.db import models
from .team import Team

class Matches(models.Model):
    team_one = models.ForeignKey(Team, related_name='team_one', on_delete=models.CASCADE, null=False)
    team_two = models.ForeignKey(Team, related_name='team_two', on_delete=models.CASCADE, null=False)
    goals_team_one = models.CharField(max_length=2, null=True)
    goals_team_two = models.CharField(max_length=2, null=True)
    status = models.CharField(max_length=30, null=True)
    data_start = models.DateField(null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.team_one.name + ' vs ' + self.team_two.name
