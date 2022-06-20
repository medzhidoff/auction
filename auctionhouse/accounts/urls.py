
from django.urls import path, include
from . import views as accounts_views

urlpatterns = [
    path('', accounts_views.profile, name='profile'),
    path('created/', accounts_views.profile_created_items, name="profile-created-items")
]