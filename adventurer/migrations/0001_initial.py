# Generated by Django 3.1.2 on 2020-10-14 04:44

import adventurer.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('adventurers', models.ManyToManyField(blank=True, related_name='adventurers', to=settings.AUTH_USER_MODEL)),
                ('dm', models.ForeignKey(blank=True, null=True, on_delete=models.SET(adventurer.models.get_sentinel_user), related_name='dm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('applets', models.ManyToManyField(blank=True, related_name='applets', to='adventurer.Applet')),
            ],
        ),
        migrations.CreateModel(
            name='Adventurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('the_surface', 'The Surface'), ('rain', 'Rain')], default='The Surface', max_length=256)),
                ('nav_style', models.CharField(choices=[('sidebar_basic', 'Basic Sidebar')], default='Sidebar Old', max_length=256)),
                ('dashboards', models.ManyToManyField(blank=True, related_name='dashboards', to='adventurer.Dashboard')),
            ],
        ),
    ]
