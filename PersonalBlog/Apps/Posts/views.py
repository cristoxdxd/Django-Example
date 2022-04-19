from django.shortcuts import render
from .models import Posts

pt = Posts()


# Create your views here.
def index(request):
    return render(request, 'index.html')


def history(request):
    return render(request, 'history.html')


def hobbies(request):
    return render(request, 'hobbies.html')


def education(request):
    return render(request, 'education.html')


def posts(request):
    post_list = pt.get_all_posts()
    context = {'posts': post_list}
    return render(request, 'posts.html', context)


def makepost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        pt.make_post(title, description)
    return render(request, 'makepost.html')
