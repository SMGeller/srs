from django.contrib import admin
from .models import Notefile, Notecard, Directory, Video, Audio, Document

admin.site.register(Notefile)
admin.site.register(Notecard)
admin.site.register(Directory)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Document)
