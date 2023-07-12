from django.shortcuts import render, get_object_or_404
from .models import Prompt, Category
from django.core.paginator import Paginator 
from django.http import JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string
# Create your views here.

def browser(request): 
    prompts = Prompt.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(prompts, 6)
    page_number = request.GET.get('page')
    page_prompts = paginator.get_page(page_number)

    return render(request, 'prompt/browser.html', {
        'prompts': prompts,
        'categories': categories,
        'page_prompts': page_prompts
    })

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

def filterData(request):
    if request.method == "POST":
        selected_category = request.POST.get('category')
        selected_language = request.POST.get('language')
        selected_difficulty = request.POST.get('difficulty')
        query = request.POST.get('query')

        allPrompts = Prompt.objects.all()

        filter_conditions = {}

        if selected_category != 'AnyCategory':
            filter_conditions['prompt_category'] = selected_category
        
        if selected_language != 'AnyLanguage':
            filter_conditions['prompt_language'] = selected_language

        if selected_difficulty != 'AnyDifficulty':
            filter_conditions['prompt_level'] = selected_difficulty
        
        if query:
            allPrompts = allPrompts.filter(Q(prompt_title__icontains=query) | Q(prompt_language__icontains=query) |
                                           Q(prompt_level__icontains=query))
        
        prompts = allPrompts.filter(**filter_conditions) if filter_conditions else allPrompts

        paginator = Paginator(prompts, 6)
        page_number = request.GET.get('page')
        page_prompts = paginator.get_page(page_number)

        context = {'page_prompts': page_prompts}
        html = render_to_string('prompt/filtered_results.html', context)

        return JsonResponse({'html': html})
    
