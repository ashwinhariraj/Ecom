from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'ecommerce/login.html'

# Register view for user registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the user
            return redirect('ecommerce:login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'ecommerce/register.html', {'form': form})

# View for creating products
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save the product
            return redirect('ecommerce:product_list')  # Redirect to product list page after creation
    else:
        form = ProductForm()

    return render(request, 'ecommerce/create_product.html', {'form': form})

# View to display a list of products
def product_list(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'ecommerce/product_list.html', {'products': products})
