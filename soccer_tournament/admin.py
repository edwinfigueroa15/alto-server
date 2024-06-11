from django.contrib import admin
from .models import Team, Matches

# Register your models here.
admin.site.register([Team, Matches])