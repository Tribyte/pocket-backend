# Generated by Django 3.1.2 on 2021-01-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='cards',
            field=models.ManyToManyField(blank=True, related_name='campaign_cards', to='campaigns.Card'),
        ),
    ]
