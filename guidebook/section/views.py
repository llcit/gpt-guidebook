from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect 

from prompt.models import Section, Paragraph

# Create your views here.

def detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    sections = Section.objects.all()
    paragraphs = Paragraph.objects.all()
    return render(request,'section/detail.html', {
        'section': section, 'sections': sections, 'paragraphs': paragraphs
    })

