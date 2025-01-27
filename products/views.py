from django.shortcuts import render, redirect, get_object_or_404
from colors.models import Color
from brands.models import Brand
from catalogs.models import Catalog
from .models import Product


def home(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request,'index.html', ctx)

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        color = request.POST.get('color')
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        category = request.POST.get('category')
        if name and price and image and description and color and brand and category:
            color = Color.objects.get(id=color)
            brand = Brand.objects.get(id=brand)
            category = Catalog.objects.get(id=category)
            Product.objects.create(
                name=name,
                price=price,
                image=image,
                description=description,
                color=color,
                category=category,
                brand=brand,
            )
            return redirect('home')
    color = Color.objects.all()
    brand = Brand.objects.all()
    category = Catalog.objects.all()
    ctx = {'color': color, 'brand': brand, 'category': category}
    return render(request, 'products/product-create.html', ctx)

def product_list(request):
    products = Product.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    color = request.GET.get('color')
    sort = request.GET.get('sort')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if brand:
        products = products.filter(brand=brand)
    if color:
        products = products.filter(color=color)
    if sort == 'low_to_high':
        products = products.order_by('price')
    elif sort == 'high_to_low':
        products = products.order_by('-price')
    elif sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    brand = Brand.objects.all()
    color = Color.objects.all()
    ctx = {'products': products, 'brand': brand, 'color': color}
    return render(request, 'products/product-by-category.html', ctx)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product}
    return render(request,'products/product-detail.html', ctx)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products:list')
