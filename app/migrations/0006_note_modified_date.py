# Generated by Django 4.2.4 on 2023-08-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
