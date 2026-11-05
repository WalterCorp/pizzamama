from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'date', 'heure', 'personnes', 'created_at')
    list_filter = ('date',)
    search_fields = ('nom', 'email', 'telephone')
    ordering = ('date', 'heure')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Client', {
            'fields': ('nom', 'email', 'telephone')
        }),
        ('Réservation', {
            'fields': ('date', 'heure', 'personnes', 'message')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
        }),
    )
