# Generated by Django 4.2.7 on 2023-12-01 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0014_alter_customuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
