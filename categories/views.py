from django.shortcuts import render, redirect
from .models import Category


def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        parent = request.POST.get('parent')
        if name and desc and parent:
            Category.objects.create(
                name = name,
                desc = desc,
                parent = parent,
            )
            return redirect('home')
    return render(request,'categories/category-create.html')