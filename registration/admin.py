from django.contrib import admin
from registration.models import Student
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=('fname','lname','description','image')
#admin.site.register(Student,studentAdmin)   

