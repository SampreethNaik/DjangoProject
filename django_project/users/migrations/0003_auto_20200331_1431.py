# Generated by Django 3.0.4 on 2020-03-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
