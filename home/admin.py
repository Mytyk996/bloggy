from django.contrib import admin
import home.models

# Register your models here.
@admin.register(home.models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    search_fields = ("title","author")
    licst_filter = ("publish","author")
    date_hierarchy = "data"