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

"""
    selected_category = request.POST.get('category')
    selected_language = request.POST.get('language')
    selected_difficulty = request.POST.get('difficulty')
    print("Selected category:" + selected_category + ", Selected language: " + 
          selected_language + ", Selected difficulty: " + selected_difficulty)

    prompts = Prompt.objects.all()

    if selected_category != 'AnyCategory':
        prompts = prompts.filter(category__category_name=selected_category)
    else:
        prompts = Prompt.objects.all()

    if selected_language != 'AnyLanguage':
        prompts = prompts.filter(prompt_language=selected_language)
    else:
        prompts = Prompt.objects.all()

    if selected_difficulty != 'AnyDifficulty':
        prompts = prompts.filter(prompt_level=selected_difficulty)
    else:
        prompts = Prompt.objects.all()

    html = render_to_string('prompt/filtered_results.html', {'prompts': prompts})
    return JsonResponse({'html': html})
    """

def filterData(request):
    if request.method == "POST":
        selected_category = request.POST.get('category')
        selected_language = request.POST.get('language')
        selected_difficulty = request.POST.get('difficulty')

        prompts = Prompt.objects.all()

        filter_conditions = Q()

        if selected_category != 'AnyCategory':
            filter_conditions &= Q(prompt_category=selected_category)
        
        if selected_language != 'AnyLanguage':
            filter_conditions &= Q(prompt_language=selected_language)

        if selected_difficulty != 'AnyDifficulty':
            filter_conditions &= Q(prompt_level=selected_difficulty)
        
        prompts = prompts.filter(filter_conditions)

        for prompt in prompts:
            print("Prompt language: " + prompt.prompt_language +
                  "Prompt category: " + prompt.prompt_category + 
                  "Prompt difficulty:" + prompt.prompt_difficulty)
        
        """
        if selected_category != 'AnyCategory' or selected_language != 'AnyLanguage' or selected_difficulty != 'AnyDifficulty':
            prompts = Prompt.objects.filter(prompt_category = selected_category)
            if selected_language != 'AnyLanguage':
                prompts = Prompt.objects.filter(prompt_language = selected_language)
                for prompt in prompts:
                    print("Prompt language: " + prompt.prompt_language)
                    if selected_difficulty != 'AnyDifficulty':
                        prompts = Prompt.objects.filter(prompt_level = selected_difficulty)
                        for prompt in prompts:
                            print("Prompt level: " + prompt.prompt_level)
                    else:
                        prompts = Prompt.objects.all()
        
       
        return render(request, 'prompt/filtered_results.html', {'prompts': prompts})
        #html = render_to_string('prompt/filtered_results.html', {'prompts': prompts})
        #return JsonResponse({'html': html})
         """


        return render(request, 'prompt/filtered_results.html', {'prompts': prompts})

        

    
