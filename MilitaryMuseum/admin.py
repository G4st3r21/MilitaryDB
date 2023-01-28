from django.contrib import admin
from .models.Combatants import Combatants
from .models.Pictures import Pictures
from .models.Videos import Videos
from .models.Places import Places

admin.site.register(Combatants)
admin.site.register(Pictures)
admin.site.register(Videos)
admin.site.register(Places)
