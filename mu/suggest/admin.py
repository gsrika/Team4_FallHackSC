from django.contrib import admin
from suggest.models import Dump

class DumpAdmin(admin.ModelAdmin):
    list_display=('pid', 'gp', 'gid', 'msg',
                  'name', 'nameid', 'utime',
                  'clink', 'llink', 'link')

admin.site.register(Dump, DumpAdmin)

