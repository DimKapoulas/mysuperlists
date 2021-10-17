from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.

# Home paige view
def home_page(request):
    return render(request, 'home.html')
    

# View for specific list
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})


# View for creating new list
def new_list(request):
    """Creates new list for user and redirects to it

    Parameters
    ----------
    request: Request
        The incoming request


    Returns
    -------
    redirections to created list
    """

    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

# View for creating a new item
def add_item(request, list_id):
    """
    Creates new item for selected list and redirects
    to corresponding list view

    Parameters
    ----------
    request: Request
        The incoming request
    list_id: int
        The id of related To-Do list
    
    Returns
    -------

    Raises
    ------
    ValueEror
    """
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


    

    

