from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, Paragraph, Prompt, Category
from django.core import serializers
from django.core.paginator import Paginator 

# Create your views here.

def browser(request): 
    prompts = Prompt.objects.all()
    categories = Category.objects.all()

    #option1 is categories
    #option2 is languages
    #option3 is difficulties 

    if request.method == 'POST' and 'option1' in request.POST:
        selected_category_name = request.POST.get('option1')

        if selected_category_name == 'AnyCategory':
            prompts = Prompt.objects.all()
        else:
            category = Category.objects.get(category_name=selected_category_name)
            prompts = category.prompt_set.all()

    paginator = Paginator(prompts, 6)
    page_number = request.GET.get('page')
    page_prompts = paginator.get_page(page_number)

    return render(request, 'prompt/browser.html', {
        'prompts': prompts,
        'categories': categories,
        'page_prompts': page_prompts
    })

    #prompts = Prompt.objects.all()
    #paginator = Paginator(prompts,6)
    #page_number = request.GET.get('page')
    #page_prompts = paginator.get_page(page_number)
    #categories = Category.objects.all()
    #return render(request, 'prompt/browser.html', {
     #   'prompts':prompts, 
     #   'categories':categories,
     #   'page_prompts':page_prompts
    #    })

def generator(request):
    dropdownLanguage = request.GET.get('dropdownLanguage')
    print(dropdownLanguage)
    prompts = Prompt.objects.all()
    categories = Category.objects.all()
    return render(request, 'prompt/generator.html', {'prompts':prompts, 'categories':categories}) 

def detail(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk)
    prompt_id = request.GET.get('prompt', 0)

    if prompt_id:
        prompts = prompts.filter(prompt_id=prompt_id)

    return render(request,'prompt/detail.html', {
        'prompt': prompt,
        'prompt_id': prompt_id
    })
