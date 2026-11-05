from django.db import models


class Reservation(models.Model):
    # Coordonnées du client
    nom = models.CharField(max_length=120)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)

    # Détails de la réservation
    personnes = models.PositiveSmallIntegerField()
    date = models.DateField()
    heure = models.TimeField()
    message = models.TextField(max_length=500, blank=True)

    # Horodatage automatique
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'heure']
        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'

    def __str__(self):
        return f'{self.nom} — {self.date} à {self.heure} ({self.personnes} pers.)'
