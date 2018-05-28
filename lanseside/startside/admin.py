from django.contrib import admin
from startside.models import Lanse,Lansetype,langtidslagring

# Register your models here.
admin.site.register(Lanse)      #registrerer databasene slik at man faar tilgang paa admin-siden
admin.site.register(Lansetype)
admin.site.register(langtidslagring)