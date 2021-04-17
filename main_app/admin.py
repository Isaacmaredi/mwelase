from django.contrib import admin
from .models import Project, Gallery

# Register your models here.
class ProjectAdmin (admin.ModelAdmin):
    list_display = ['id', 'user','description','client',
                    'location','start_date','end_date','status','value']
    list_display_links = ('id','description')
    list_fiter = ('client',)
    search_fields = ('client','status')
    list_per_page = 15

admin.site.register(Project,ProjectAdmin)

class GalleryAdmin (admin.ModelAdmin):
    list_display = ['id','description','place']
    list_fiter = ('description',)
    search_fields=('description','place')
    list_per_page = 15

admin.site.register(Gallery,GalleryAdmin)