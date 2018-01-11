from django.contrib import admin
from .models import Tag, Note

admin.site.register(Tag)
#admin.site.register(Note)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created')
    list_filter = ('date_created',)

admin.site.register(Note, NoteAdmin)
