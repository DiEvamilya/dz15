from django.contrib import admin

from program.models import Module, Course, Lesson

admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Lesson)