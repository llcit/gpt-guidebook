from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect 

from prompt.models import Section, Paragraph

# Create your views here.

def detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    sections = Section.objects.all()
    paragraphs = Paragraph.objects.all()
    section_id = request.GET.get('section', 0)

    if section_id:
        paragraphs = paragraphs.filter(section_id=section_id)

    return render(request,'section/detail.html', {
        'section': section, 
        'sections': sections, 
        'paragraphs': paragraphs,
        'section_id': section_id
    })

