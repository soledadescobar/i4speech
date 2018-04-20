# Register your models here.
from django.contrib import admin

from .models import Textos
from .models import Autores
from .models import Escalafh
from .models import Escalain
from .models import Escalagu
from .models import Escalasp
from .models import Escalamu
from .models import Fh
from .models import Gu
from .models import Mu
from .models import Sp
from .models import Cr
from .models import Ocasiones


# Define the admin class

@admin.register(Fh)
class FhAdmin(admin.ModelAdmin):
    pass

@admin.register(Gu)
class GuAdmin(admin.ModelAdmin):
    pass

@admin.register(Mu)
class MuAdmin(admin.ModelAdmin):
    pass

@admin.register(Sp)
class SpAdmin(admin.ModelAdmin):
    pass

@admin.register(Cr)
class CrAdmin(admin.ModelAdmin):
    pass

@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    pass
@admin.register(Textos)
class TextosAdmin(admin.ModelAdmin):
    pass

@admin.register(Escalafh)
class EscalafhAdmin(admin.ModelAdmin):
    pass

@admin.register(Escalain)
class EscalainAdmin(admin.ModelAdmin):
    pass

@admin.register(Escalagu)
class EscalaguAdmin(admin.ModelAdmin):
    pass

@admin.register(Escalasp)
class EscalaspAdmin(admin.ModelAdmin):
    pass

@admin.register(Escalamu)
class EscalamuAdmin(admin.ModelAdmin):
    pass

@admin.register(Ocasiones)
class OcasionesAdmin(admin.ModelAdmin):
    pass