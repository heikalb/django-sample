# Generated by Django 3.0.1 on 2020-01-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostpost',
            name='award',
        ),
        migrations.AddField(
            model_name='post',
            name='award',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True),
        ),
    ]
