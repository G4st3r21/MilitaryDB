from .models.Combatants import Combatants
from .models.BGPictures import BGPictures
from .models.Videos import Videos
from .models.Places import Places
from .models.Ranks import Ranks
from .models.Pictures import Pictures

from django.contrib import admin

admin.site.register(Combatants)
admin.site.register(Pictures)
admin.site.register(BGPictures)
admin.site.register(Places)
admin.site.register(Videos)
admin.site.register(Ranks)
