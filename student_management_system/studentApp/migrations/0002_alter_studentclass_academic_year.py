# Generated by Django 5.1.5 on 2025-06-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclass',
            name='academic_year',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
