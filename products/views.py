from django.shortcuts import render, redirect, get_object_or_404
from brands.models import Brand
from categories.models import Category
from colors.models import Color
from .models import Product, Comment


def home(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request,'index.html', ctx)

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        color = request.POST.get('color')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        if name and price and brand and category and color and desc and image:
            brand = Brand.objects.get(id=brand)
            color = Color.objects.get(id=color)
            category = Category.objects.get(id=category)
            Product.objects.create(
                name = name,
                price = price,
                brand = brand,
                category = category,
                color = color,
                desc = desc,
                image = image,
            )
            return redirect('home')
    brands = Brand.objects.all()
    categories = Category.objects.all()
    colors = Color.objects.all()
    ctx = {'brands': brands, 'categories': categories, 'colors': colors }
    return render(request,'products/product-create.html', ctx)

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
    brands = Brand.objects.all()
    colors = Color.objects.all()
    ctx = {'products': products, 'brands': brands, 'colors': colors }
    return render(request, 'products/product-by-category.html', ctx)

def product_detail(request, pk, year, month, day, slug):
    product = get_object_or_404(
        Product,
        pk=pk,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        if name and rating and review:
            Comment.objects.create(
                name = name,
                rating = rating,
                review = review,
                product = product,
            )
            return redirect('products:detail', pk=pk, year=year, month=month, day=day, slug=slug )
    comments = product.comments.all()
    ctx = {'product': product, 'comments': comments }
    return render(request,'products/product-detail.html', ctx)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products:list')