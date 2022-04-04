from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    title = 'Instagram - Home'

    context = {'title': title}
    return render(request, 'insta/index.html', context)


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


def profile(request, uid):
    # todo Get title of page from the user details
    my_range = range(0, 9)
    context = {"title": "placeholder", 'my_range':my_range}
    return render(request, 'insta/profile.html', context)
