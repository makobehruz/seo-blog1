from django.shortcuts import render, redirect
from .models import Color


def color_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if name and color:
            Color.objects.create(
                name = name,
                color = color,
            )
            return redirect('home')
    return render(request,'colors/color-create.html')


