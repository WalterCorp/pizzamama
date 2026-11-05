from django.db import migrations, models


def seed_pizza_v2(apps, schema_editor):
    Pizza = apps.get_model('menu', 'Pizza')

    updates = {
        'Végétarienne': {
            'description': 'Une recette colorée et généreuse avec une base tomate, des légumes grillés et une finition pleine de fraîcheur.',
            'categorie': 'veggie',
            'image_url': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1200&q=80',
            'signature': True,
        },
        'Barbecue': {
            'description': 'Une pizza gourmande et intense, pensée pour les amateurs de saveurs fumées et de générosité.',
            'categorie': 'signature',
            'image_url': 'https://images.unsplash.com/photo-1548365328-9f547fb0953b?auto=format&fit=crop&w=1200&q=80',
            'signature': True,
        },
        'Tuna': {
            'description': 'Une recette équilibrée mêlant thon, oeuf et poivron sur une base tomate simple et efficace.',
            'categorie': 'classique',
            'image_url': 'https://images.unsplash.com/photo-1594007654729-407eedc4be65?auto=format&fit=crop&w=1200&q=80',
            'signature': False,
        },
        '4 Fromages': {
            'description': 'Une composition riche et fondante avec quatre fromages sélectionnés pour une vraie sensation de confort.',
            'categorie': 'veggie',
            'image_url': 'https://images.unsplash.com/photo-1574126154517-d1e0d89ef734?auto=format&fit=crop&w=1200&q=80',
            'signature': True,
        },
        'Norvégienne': {
            'description': 'Une pizza à base crème fraîche et saumon, plus raffinée, idéale pour une carte premium.',
            'categorie': 'blanche',
            'image_url': 'https://images.unsplash.com/photo-1511689660979-10d2b1aada49?auto=format&fit=crop&w=1200&q=80',
            'signature': False,
        },
        'Marguerita': {
            'description': 'L’incontournable de la maison, volontairement simple, légère et rassurante.',
            'categorie': 'classique',
            'image_url': 'https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?auto=format&fit=crop&w=1200&q=80',
            'signature': False,
        },
        'Western': {
            'description': 'Une base crème très gourmande avec poulet fumé, pommes de terre et Boursin pour une vraie identité produit.',
            'categorie': 'blanche',
            'image_url': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1200&q=80',
            'signature': True,
        },
    }

    for pizza in Pizza.objects.all():
        data = updates.get(pizza.nom)
        if not data:
            continue
        pizza.description = data['description']
        pizza.categorie = data['categorie']
        pizza.image_url = data['image_url']
        pizza.signature = data['signature']
        pizza.disponible = True
        pizza.save(update_fields=['description', 'categorie', 'image_url', 'signature', 'disponible'])


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='categorie',
            field=models.CharField(choices=[('classique', 'Classique'), ('blanche', 'Base crème'), ('signature', 'Signature'), ('veggie', 'Végétarienne')], default='classique', max_length=20),
        ),
        migrations.AddField(
            model_name='pizza',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='signature',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(seed_pizza_v2, migrations.RunPython.noop),
    ]
