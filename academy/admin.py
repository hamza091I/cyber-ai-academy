from django.contrib import admin
from .models import Course, Enrollment, ContactMessage

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(ContactMessage)