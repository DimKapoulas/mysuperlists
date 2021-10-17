from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

# Home paige view
def home_page(request):
    # User input given
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    
    # If GET request
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

# View for specific list
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
