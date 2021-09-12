from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import WishList
from .forms import ProductForm



def index(request):
	return render(request, 'main/index.html', {})

def about(request):
	return render(request, 'main/about.html')

def store(request):
	return render(request, 'main/store.html')

def feedback_base(request):
	return render(request, 'main/feedback.html')

def feedback(request, pk):
	"""view page the wishlist"""
	wishlist = get_object_or_404(WishList, pk=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST)
		instance_product = form.save()
		wishlist.product.add(instance_product)
		wishlist.save()
	elif request.method == 'GET':
		form = ProductForm()


	return render(
		request,
		'main/feedback.html',
		{
			'wishlist': wishlist,
			"is_owner_list": wishlist.owner == request.user,
			'form': form
		}
	)