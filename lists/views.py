from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.


def home_page(request):
    # User input given
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    # If GET request
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
