# Generated by Django 3.1.3 on 2020-11-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='has_submenu',
            field=models.IntegerField(default=None),
        ),
    ]