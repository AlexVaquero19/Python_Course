from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Author, Book, User
from .forms import AuthorForm, UsersForm

# Create your views here.
def home(request):
    return render(request, 'my_app_activity/home.html')

def about(request):
    return render(request, 'my_app_activity/about.html')

def api_data(request):
    data = { "name": "Alejandro", "age": 25, "city": "Madrid" } 
    return JsonResponse(data)

def others(request):
    return render(request, 'my_app_activity/others.html')

def author_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_view') 
    else:
        form = AuthorForm()

    authors = Author.objects.all()  # Obtiene todos los autores
    return render(request, 'my_app_activity/authors.html', {'form': form, 'authors': authors})

def users_view(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_view') 
    else:
        form = UsersForm()

    users = User.objects.all()  # Obtiene todos los autores
    return render(request, 'my_app_activity/users.html', {'form': form, 'users': users})

def profile(request):
    context = {
        'username': 'Alejandro',
        'is_active': True,
        'projects': [
            {'name': 'Project A', 'status': 'Completed'},
            {'name': 'Project B', 'status': 'In Progress'},
            {'name': 'Project C', 'status': 'Not Started'}
        ]
    }
    return render(request, 'my_app_activity/profile.html', context)

def about_2(request):
    return render(request, 'my_app_activity/about_2.html')

def base_with_logo(request):
    return render(request, 'my_app_activity/base_with_logo.html')

def base_with_js(request):
    return render(request, 'my_app_activity/base_with_js.html')