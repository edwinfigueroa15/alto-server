from django.contrib import admin
from soccer_tournament.models.team import Team
from soccer_tournament.models.matches import Matches

# Register your models here.
admin.site.register([Team, Matches])