from django.shortcuts import render, get_object_or_404

from .models import WishList

# Create your views here.

def index(request):
	return render(request, 'main/index.html', {})

def about(request):
	return render(request, 'main/about.html')

def store(request):
	return render(request, 'main/store.html')

def feedback(request, pk):
	"""
	FBV - views основаны на функциях 
	CBV - views основаны на классах 
	"""
	wishlist = get_object_or_404(WishList, pk=pk)
	print('[wishlist]', wishlist)
	return render(
		request,
		'main/feedback.html', 
		{
			'wishlist':wishlist,
			"is_owner_list": wishlist.owner == request.user
		}
	)