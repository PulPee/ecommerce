# Generated by Django 2.1.2 on 2018-11-04 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='upperCategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='ProductManager.Category'),
        ),
    ]
