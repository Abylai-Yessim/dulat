# Generated by Django 4.2.7 on 2023-12-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]
