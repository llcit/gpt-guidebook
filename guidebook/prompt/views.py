from django.shortcuts import render, redirect
from .models import Section, Paragraph

# Create your views here.

def guidebook(request):
    sections = Section.objects.all()
    paragraphs = Paragraph.objects.all()
    return render(request, 'prompt/guidebook.html', {'sections':sections, 'paragraphs':paragraphs})