# Generated by Django 4.2.4 on 2023-08-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_tag_articles_scope_article_scope_tag_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='is_main',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
