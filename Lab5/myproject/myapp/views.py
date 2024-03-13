from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

def add_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        new_person = Person(username=username, password=password)
        people.append(new_person)

    return render(request, 'myapp/add.html')

def display_view(request):
    return render(request, 'myapp/display.html', {'people': people})