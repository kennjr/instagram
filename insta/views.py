from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.
from insta.models import User, Profile, LocalUser, Post


@login_required(login_url='/login')
def logout_method(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def home(request):
    title = 'Instagram - Home'
    posts = Post.objects.all()

    context = {'title': title, 'posts': posts}
    return render(request, 'insta/index.html', context)


@login_required(login_url='/login')
def new_post(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)

        caption = request.POST.get('caption_field')
        location = request.POST.get('location_field')
        user = request.user
        image_url = file_url
        Post.objects.create(user=user, location=location, caption=caption, image_url=image_url)
        return redirect('/')
    context = {"title": 'New Post'}
    return render(request, 'insta/follow_msg.html', context)


@login_required(login_url='/login')
def search(request):
    title = 'Instagram - Home'
    search_req = request.GET.get('q') if request.GET.get('q') is not None else ''

    if search_req == '':
        is_req_empty = True
    else:
        # todo Make a search request for posts with a location/user/caption that matches the str
        is_req_empty = False
    context = {'title': title}
    return render(request, 'insta/search.html', context)


@login_required(login_url='/login')
def profile(request, uid):
    # todo Get title of page from the user details
    my_range = range(0, 9)
    context = {"title": "placeholder", 'my_range':my_range}
    return render(request, 'insta/profile.html', context)


def login_page(request):
    auth_req = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        # Getting the user's info
        username = request.POST.get('identifier_field')
        password = request.POST.get('password_field')
        # Checking if the user exists
        try:
            user = User.objects.get(username=username)
            # The authenticate fun below will either return a user obj. tha matches the cred.s we've provides or None
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # The login fun will add a session for the user logging them in
                login(request, user)

                # Once the user has been logged in successfully we wanna redirect them to the home page
                return redirect('/')
            else:
                messages.error(request, "The username and password don't matches")

        except :
            messages.error(request, "The username and password don't match")

    context = {'title': "Login", 'auth_req': auth_req}
    return render(request, 'insta/login_register.html', context)


def register_page(request):
    auth_req = 'register'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        # Getting the user's info
        username = request.POST.get('username_field')
        name = request.POST.get('name_field')
        email = request.POST.get('email_field')
        password = request.POST.get('password_field')
        # Checking if the user exists
        try:
            user = User.objects.get(username=username)

            if user is None:
                new_user = User.objects.create_user(username=username, email=email, password=password)

                LocalUser.objects.create(user=new_user, name=name, email=email)
                Profile.objects.create(user=new_user, bio='', website='')
                # Once the user has been logged in successfully we wanna redirect them to the home page
                print("The creation was successful")
                return redirect('/login')
            else:
                print("The creation was not successful")
                messages.error(request, "The username and password don't matches")

        except :
            new_user = User.objects.create_user(username=username, email=email, password=password)

            LocalUser.objects.create(user=new_user, name=name, email=email)
            Profile.objects.create(user=new_user, bio='', website='')
            # Once the user has been logged in successfully we wanna redirect them to the home page
            print("The creation was successful")
            print("The creation was nott successful")
            messages.error(request, "The username and password don't match")

    context = {'title': "Register", 'auth_req': auth_req}
    return render(request, 'insta/login_register.html', context)


@login_required(login_url="/login")
def post_page(request, post_id):
    context = {"title": "Post"}
    return render(request, 'insta/view_post.html', context)

