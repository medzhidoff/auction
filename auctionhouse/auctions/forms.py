from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import Auction, Bid, Item, ItemCategory
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime


class AddBidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(AddBidForm, self).__init__(*args, **kwargs)
       self.fields['price'].widget.attrs['readonly'] = True

    class Meta:
        model = Bid
        fields = ['price', 'auction', 'user']
        exclude = ('auction', 'user')
        widgets = {
            'auction': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }


class AddAuctionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        print(user)
        items_to_sell = Item.objects.filter(owner__exact=user)
        self.fields['item'].queryset = items_to_sell

    class Meta:
        model = Auction
        fields = ['item', 'start_price', 'date_expired']
        labels = {
            "start_price": "Starting Price"
        }


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)


class AddItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'border border-coolGray-300 rounded w-full text-coolGray-600 placeholder-coolGray-400 transition duration-500 focus:shadow-lg focus:border-teal-400 focus:outline-none px-4 py-3',
            'placeholder': 'eg: Cybar Boss &amp; Mega Boss #3 '
        }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'border border-coolGray-300 rounded w-full text-coolGray-600 placeholder-coolGray-400 transition duration-500 focus:shadow-lg focus:border-teal-400 focus:outline-none px-4 py-3',
            'placeholder': 'eg: Cybar Boss &amp; Mega Boss #3 '
        }
    ))

    image = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'h-full w-full opacity-0',
        }
    ))
    # category = forms.ChoiceField(widget=forms.RadioSelect)

    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'category', 'status']
