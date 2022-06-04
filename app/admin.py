from django.contrib import admin
from app.models import Task, User, Status, Label


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task)


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User)


class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status)


class LabelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Label)
