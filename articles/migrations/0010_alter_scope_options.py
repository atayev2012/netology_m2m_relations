# Generated by Django 4.2.4 on 2023-08-02 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_scope_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main'], 'verbose_name': 'Тематики статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]
