from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'Gold Nugget'
    value = 1000
    context = { 'treasure_name': name, 'treasure_value': value }
    return render(request, 'index.html', context)