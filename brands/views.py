from django.shortcuts import render, redirect
from .models import Brand


def brand_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        logo = request.FILES.get('logo')
        print(name, desc, logo)
        if name and desc and logo:
            Brand.objects.create(
                name = name,
                desc = desc,
                logo = logo,
            )
            return redirect('home')
    return render(request,'brands/brand-create.html')

