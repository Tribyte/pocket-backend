# Generated by Django 3.1.2 on 2021-01-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20210101_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='card_notes', to='campaigns.Note'),
        ),
        migrations.AlterField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='card_tags', to='campaigns.Tag'),
        ),
    ]