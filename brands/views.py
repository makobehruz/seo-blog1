from django.shortcuts import render, redirect
from .models import Brand


def brand_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        if name and description and image:
            Brand.objects.create(
                name = name,
                description = description,
                image = image,
            )
            return redirect('home')
    return render(request,'brands/brand-create.html')


