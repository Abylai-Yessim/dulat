# Generated by Django 4.2.7 on 2023-12-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0009_customuser_phone_number_alter_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
