from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'Instagram - Home'
    search_req = request.GET.get('search_str') if request.GET.get('search_str') is not None else ''

    if search_req != '':
        context = {'title': title, 'mode': "browse"}
    else:
        context = {'title': title, 'mode': "search"}
    return render(request, 'insta/index.html', context)

