# Generated by Django 3.1.5 on 2022-07-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20220704_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='mindg',
            field=models.IntegerField(blank=True, db_index=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='execution',
            name='mind1',
            field=models.IntegerField(blank=True, db_index=True, default=0, null=True),
        ),
    ]