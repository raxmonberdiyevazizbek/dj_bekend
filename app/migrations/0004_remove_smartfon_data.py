# Generated by Django 5.0.2 on 2024-03-02 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_smartfon_memory_alter_smartfon_ram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartfon',
            name='data',
        ),
    ]
