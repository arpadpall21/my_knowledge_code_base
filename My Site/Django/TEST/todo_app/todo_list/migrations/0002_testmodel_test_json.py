# Generated by Django 4.1.5 on 2023-01-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='test_json',
            field=models.JSONField(null=True),
        ),
    ]
