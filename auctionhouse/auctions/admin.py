from django.contrib import admin
from .models import Auction, Bid, Comment, Item, ItemCategory

# Register your models here.

admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Item)
admin.site.register(ItemCategory)