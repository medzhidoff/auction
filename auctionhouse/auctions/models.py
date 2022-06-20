from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from datetime import datetime, timedelta
from PIL import Image
import pytz
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
CONDITION_CHOICES = [
    ('New', 'New'),
    ('Used', 'Used'),
    ('Brand New', 'Brand New'),
    ('Like New', 'Like New'),
    ('Very Good', 'Very Good'),
    ('New with tags', 'New with tags'),
    ('New without tags', 'New without tags'),
    ('New with defects', 'New with defects'),
    ('For parts or not working', 'For parts or not working'),
    ('Seller refurbished', 'Seller refurbished'),
]

STATUS_CHOICES = [
    ('ONSALE', 'На продаже'),
    ('SOLD', 'Продан'),
    ('HIDDEN', 'Скрыт'),
]


class ItemCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='images_auctions')

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lot_number = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='images_items')
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('ItemCategory', null=True, blank=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_creator')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_owner')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk' : self.pk})


class Auction(models.Model):

    date_created = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', blank=False, null=True, on_delete=models.CASCADE, related_name='item')
    # Variables to save having to traverse through all bids etc here
    start_price = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    fixed_price = models.PositiveIntegerField(default=0)
    amount_of_bids = models.IntegerField(default=0)
    winnerBid = models.ForeignKey('Bid', blank=True, null=True, on_delete=models.CASCADE, related_name='winner')
    closed = models.BooleanField(default=False)


    @property
    def expired(self):
        expiry = self.date_expired.replace(tzinfo=None)
        now = timezone.now().replace(tzinfo=None)
        if now > expiry:
            return True
        return False

    def __str__(self):
        return self.item.title

    def get_absolute_url(self):
        return reverse('auction-detail', kwargs={'pk' : self.pk})

    
class Bid(models.Model):
    price = models.IntegerField(default=1)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    winningBid = models.BooleanField(default=False)


class Comment(models.Model):
	auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField()
	date_created = models.DateTimeField()




