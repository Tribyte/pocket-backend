# Generated by Django 3.1.2 on 2021-01-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_auto_20210101_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='campaign_tags', to='campaigns.Tag'),
        ),
    ]
