# Generated by Django 5.0 on 2023-12-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_clue'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='teamName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
