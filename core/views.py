from django.shortcuts import redirect, render

from item.models import Item
from item.models import Category, Item
from core.forms import SignupForm
# Create your views here.
def index(request):
    items= Item.objects.filter(is_sold=False)[0:10]
    categories= Category.objects.all()
    context={"categories": categories, "items":items}
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else: 
        form = SignupForm();
        
    return render(request, 'core/signup.html', {"form": form})