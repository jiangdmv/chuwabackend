# Generated by Django 4.0.5 on 2022-06-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_newuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='role',
            field=models.JSONField(default=['user']),
        ),
    ]
