from django.shortcuts import render, get_object_or_404
from .models import Prompt, Category, SimplePage, Section, Paragraph, Subparagraph
from django.core.paginator import Paginator 
from django.http import JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string
# Create your views here.

def index(request, pk):
    section = get_object_or_404(Section, pk=pk)
    sections = Section.objects.all()
    paragraphs = Paragraph.objects.all()
    subparagraphs = Subparagraph.objects.all()
    section_id = request.GET.get('section', 0)

    if section_id:
        paragraphs = paragraphs.filter(section_id=section_id)

    return render(request,'prompt/index.html', {
        'section': section, 
        'sections': sections, 
        'paragraphs': paragraphs,
        'subparagraphs': subparagraphs,
        'section_id': section_id
    })
    

def promptgeneratorinfo(request):
    return render(request, 'prompt/promptgeneratorinfo.html')

def promptbrowserinfo(request):
    return render(request, 'prompt/promptbrowserinfo.html')

def about(request):
    about_page = get_object_or_404(SimplePage, slug='about')
    return render(request, 'prompt/about.html', {'title': about_page.title, 'content': about_page.text})

def browser(request):
    prompts = Prompt.objects.all()
    categories = Category.objects.all()

    return render(request, 'prompt/browser.html', {
        'prompts': prompts,
        'categories': categories,
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

def filteredResults(request):
    categories = Category.objects.all()
    return render(request,'prompt/filtered_results.html', {
        'categories': categories 
    })

