# Generated by Django 2.0.2 on 2022-05-12 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20220513_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagefull',
        ),
    ]
