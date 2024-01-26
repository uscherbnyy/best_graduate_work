from django.contrib import admin

from ToDo.models import UserProfile, Task, Category, Priority

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Priority)