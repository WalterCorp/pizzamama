from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_pizza_v2_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image_url',
            field=models.CharField(blank=True, help_text="Chemin d'image local dans static/, ex : menu/images/pizzas/marguerita.png", max_length=255),
        ),
    ]
