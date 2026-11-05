from django.db import models


class Pizza(models.Model):
    CATEGORIES = [
        ('classique', 'Classique'),
        ('blanche', 'Base crème'),
        ('signature', 'Signature'),
        ('veggie', 'Végétarienne'),
    ]

    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='classique')
    image_url = models.CharField(
    max_length=255,
    blank=True,
    help_text="Chemin d'image local dans static/, ex : menu/images/pizzas/marguerita.png"
)
    disponible = models.BooleanField(default=True)
    signature = models.BooleanField(default=False)

    class Meta:
        ordering = ['prix', 'nom']

    def __str__(self):
        return str(self.nom)

    @property
    def category_label(self):
        return self.get_categorie_display()
