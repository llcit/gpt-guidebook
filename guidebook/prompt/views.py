from django.shortcuts import render, redirect
from .models import Section, Paragraph, Prompt, Category
from django.core import serializers
from django.core.paginator import Paginator 

# Create your views here.

def browser(request): 
    prompts = Prompt.objects.all()
    paginator = Paginator(prompts,6)
    page_number = request.GET.get('page')
    page_prompts = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'prompt/browser.html', {
        'prompts':prompts, 
        'categories':categories,
        'page_prompts':page_prompts
        })

def generator(request):
    dropdownLanguage = request.GET.get('dropdownLanguage')
    print(dropdownLanguage)
    prompts = Prompt.objects.all()
    categories = Category.objects.all()
    return render(request, 'prompt/generator.html', {'prompts':prompts, 'categories':categories}) 