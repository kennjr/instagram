from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'Instagram - Home'
    context = {'title': title}
    return render(request, 'insta/index.html', context)

