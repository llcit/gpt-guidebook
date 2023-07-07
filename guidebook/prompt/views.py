from django.shortcuts import render, redirect
from .models import Section, Paragraph, Prompt, Category
from django.core import serializers

# Create your views here.

def browser(request): 
    prompts = Prompt.objects.all()
    categories = Category.objects.all()
    return render(request, 'prompt/browser.html', {'prompts':prompts, 'categories':categories})

def generator(request):
    dropdownLanguage = request.GET.get('dropdownLanguage')
    print(dropdownLanguage)
    prompts = Prompt.objects.all()
    categories = Category.objects.all()
    return render(request, 'prompt/generator.html', {'prompts':prompts, 'categories':categories}) 