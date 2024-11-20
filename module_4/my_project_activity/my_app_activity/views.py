from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Author, Book, User
from .forms import AuthorForm, UsersForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from rest_framework import viewsets, generics
from .serializers import BookSerializer, AuthorSerializer

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # Redirects the user to the login page
    else:
        form = UserCreationForm()
    return render(request, 'my_app_activity/register.html', {'form': form})

@login_required
def protected_profile(request):
    return render(request, 'my_app_activity/protected_profile.html')

@login_required
def modify_user(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'my_app_activity/modify.html', {'form': form})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    