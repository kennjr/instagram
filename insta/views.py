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
