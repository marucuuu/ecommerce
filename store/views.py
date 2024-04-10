from django.shortcuts import redirect, render
from .models import Order

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')

        # Save the form data to the database
        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            country=country
        )
        order.save()
		
        # Redirect to a success page or any other page as per your requirement
        
    context = {}
    return render(request, 'store/checkout.html', context)
