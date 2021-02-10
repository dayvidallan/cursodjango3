from django.contrib import admin
from .models import Post, Contact, Perfil


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'sub_title', 'full_name', 
        'categories', 'deleted'
    ]
    search_fields = ['title', 'sub_title']
    #fields = ('title', 'sub_title')

    #def get_queryset(self, request):
    #    return Post.objects.filter(deleted=False)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['name', 'especialidade', 'nrTelCelular', 'texto']
    search_fields = ['name', 'especialidade', 'nrTelCelular', 'texto']

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(Perfil, PerfilAdmin)
