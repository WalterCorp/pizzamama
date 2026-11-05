from django.contrib import admin
from .models import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'vegetarienne', 'signature', 'disponible')
    list_filter = ('categorie', 'vegetarienne', 'signature', 'disponible')
    search_fields = ('nom', 'ingredients', 'description')
    list_editable = ('prix', 'signature', 'disponible')
    ordering = ('prix', 'nom')
    fieldsets = (
        ('Identité', {
            'fields': ('nom', 'categorie', 'description')
        }),
        ('Contenu', {
            'fields': ('ingredients', 'image_url'),
            'description': 'Utiliser un chemin local vers un visuel stocké dans static/, par exemple menu/images/pizzas/marguerita.png'
        }),
        ('Commercial', {
            'fields': ('prix', 'vegetarienne', 'signature', 'disponible')
        }),
    )
