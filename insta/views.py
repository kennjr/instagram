from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
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
    search_filter = 'posts'

    title = 'Instagram - Home'
    search_req = request.GET.get('q') if request.GET.get('q') is not None else ''

    if search_req == '':
        is_req_empty = True
        users = None
        posts = None
        users_count = 0
        posts_count = 0
    else:
        # Check for the filter
        if search_filter == "posts":
            posts = Post.objects.filter(
                Q(user__username__icontains=search_req) |
                Q(location__icontains=search_req) |
                Q(caption__icontains=search_req)
            ).all()
            posts_count = posts.count()
            users_count = 0
            users = None
        else:
            users = User.objects.filter(
                Q(username__icontains=search_req)
            )
            users_count = users.count()
            posts_count = 0
            posts = None
        # todo Make a search request for posts with a location/user/caption that matches the str
        is_req_empty = False
    context = {'title': title, 'posts_results': posts, 'users_results': users, 'posts_count': posts_count,
               'users_count': users_count, "is_req_empty": is_req_empty, 'filter': search_filter, 'search_str': search_req}
    return render(request, 'insta/search.html', context)


@login_required(login_url='/login')
def profile(request, uid):
    posts = Post.objects.filter(Q(user__id=request.user.id)).all()
    profile_info = Profile.objects.get(user__id=request.user.id)
    user_info = User.objects.get(user__id=request.user.id)
    context = {"title": user_info.username, 'posts': posts, 'profile_info': profile_info, 'user_info': user_info}
    return render(request, 'insta/profile.html', context)


@login_required(login_url='/login')
def user_page(request):
    posts = Post.objects.filter(user__id=request.user.id).all()
    profile_info = Profile.objects.filter(user__id=request.user.id)
    user_info = User.objects.filter(id=request.user.id).first()
    context = {"title": user_info.username, 'posts': posts, 'profile_info': profile_info, 'user_info': user_info}
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
            return redirect('/login')
            # messages.error(request, "The username and password don't match")

    context = {'title': "Register", 'auth_req': auth_req}
    return render(request, 'insta/login_register.html', context)


@login_required(login_url="/login")
def post_page(request, post_id):
    context = {"title": "Post"}
    return render(request, 'insta/view_post.html', context)

