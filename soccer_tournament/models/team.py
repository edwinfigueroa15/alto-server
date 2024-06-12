
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    position = models.CharField(max_length=2, null=True)
    points = models.CharField(max_length=3, null=True)
    matches_won = models.CharField(max_length=2, null=True)
    lost_matches = models.CharField(max_length=2, null=True)
    tied_matches = models.CharField(max_length=2, null=True)
    goals_favor = models.CharField(max_length=2, null=True)
    goals_against = models.CharField(max_length=2, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['position']