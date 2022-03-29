from django.contrib import admin

# Register your models here.
from networks.models import Network, Connection

admin.site.register(Network)
admin.site.register(Connection)