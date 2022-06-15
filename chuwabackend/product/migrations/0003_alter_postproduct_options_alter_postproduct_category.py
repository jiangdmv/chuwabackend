# Generated by Django 4.0.5 on 2022-06-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postproduct',
            options={'ordering': ('-published',)},
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='category',
            field=models.ForeignKey(default='Computer', on_delete=django.db.models.deletion.PROTECT, to='product.category'),
        ),
    ]
