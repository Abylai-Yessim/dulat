# Generated by Django 4.2.7 on 2023-12-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0010_alter_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
