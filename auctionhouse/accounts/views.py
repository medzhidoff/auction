from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, UpdateProfileForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from auctions.models import Auction, Item
from django.http import Http404
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        print("post")
        form = UserLoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("form valid")
            username = request.POST['username']
            password = request.POST['password']
            print(username + ' ' + password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("user not none none")
                return redirect(reverse('profile'))
        else:
            print(form.errors)
            print("form invalid")
            return render(request, 'accounts/login.html', {'form': form})
    else:

        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            # creates the user object in the table
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acccount created for {username}!')
            return redirect('login')
    else:
        # registration form inbuilt django
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# decorator to make sure user is logged in
@login_required
def profile(request):

    # Pass all auctions that I won here...

    # First find all those that are closed
    auctions = Auction.objects.filter(closed=True)
    owned_items = Item.objects.filter(owner__exact=request.user)
    print('sdsdsd')
    print(owned_items)
    # Now find the winningBid is equal to me
    myWins = []
    for aucs in auctions:
        # Are there any winning bids on this auction?
        if aucs.winnerBid:
            # Am i the winning bid?
            if aucs.winnerBid.user == request.user:
                myWins.append(aucs)

    context = {
        'owned_items': owned_items,
    }

    return render(request, 'accounts/profile.html', context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        updateProfileForm = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # save profiles if valid
        if updateUserForm.is_valid() and updateProfileForm.is_valid():
            updateUserForm.save()
            updateProfileForm.save()
            messages.success(request, f'Acccount updated!')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)
        updateProfileForm = UpdateProfileForm(instance=request.user.profile)
    pass


@login_required
def profile_created_items(request):
    created_items = Item.objects.filter(creator__exact=request.user)
    context = {
        'created_items': created_items,
    }

    return render(request, 'accounts/profile_created_items.html', context)
