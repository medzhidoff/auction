# Generated by Django 3.2.13 on 2022-06-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
