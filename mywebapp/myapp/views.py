from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
## import todo form and models

from .forms import TodoForm
from .models import myapp

###############################################

def index(request):

	item_list = myapp.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp')
	form = TodoForm()

	page = {
			"forms" : form,
			"list" : item_list,
			"title" : "TODO LIST",
		}
	return render(request, 'index.html', page)



### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = myapp.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('myapp')
