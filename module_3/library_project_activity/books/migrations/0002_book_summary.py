# Generated by Django 5.1.3 on 2024-11-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
