from django.shortcuts import render, redirect
from catalogs.models import Catalog


def catalog_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if name and description:
            Catalog.objects.create(
                name = name,
                description = description,

            )
            return redirect('home')
    return render(request,'catalogs/category-create.html')

