from django.contrib import admin

# Register your models here.

from .models import Talkgroup, Owner, Bridge, Server

@admin.register(Owner)
class TalkgroupAdmin(admin.ModelAdmin):
    list_display = [ 'shortname', 'name', ]


@admin.register(Talkgroup)
class TalkgroupAdmin(admin.ModelAdmin):
    list_display = [ 'tgid', 'name', 'owner', 'created_at', 'updated_at' ]

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = [ 'network_id', 'server_name', 'name', 'hostname', 'hotspot_port', 'listed', 'hotspot_allow', 'created_at', 'updated_at' ]

@admin.register(Bridge)
class TalkgroupAdmin(admin.ModelAdmin):
    list_display = [ 'talkgroup', 'mode', 'target', 'network', 'description', 'public', 'operator', ]

