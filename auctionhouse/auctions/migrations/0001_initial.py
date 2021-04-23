# Generated by Django 3.2 on 2021-04-23 04:59

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Brand New', 'Brand New'), ('Like New', 'Like New'), ('Very Good', 'Very Good'), ('New with tags', 'New with tags'), ('New without tags', 'New without tags'), ('New with defects', 'New with defects'), ('For parts or not working', 'For parts or not working'), ('Seller refurbished', 'Seller refurbished')], default='New', max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='images_auctions')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_expired', models.DateTimeField(default=datetime.datetime(2021, 4, 30, 5, 59, 37, 386225))),
                ('price', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('amount_of_bids', models.IntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('winningBid', models.BooleanField(default=False)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='winnerBid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='auctions.bid'),
        ),
    ]