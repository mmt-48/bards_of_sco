# Generated by Django 3.1.5 on 2022-07-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_execution_note1'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='mind',
            field=models.IntegerField(blank=True, db_index=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='execution',
            name='mind',
            field=models.IntegerField(blank=True, db_index=True, default=0, null=True),
        ),
    ]
