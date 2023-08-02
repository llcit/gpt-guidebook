from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_information = models.TextField(null=True)
    category_svg = models.TextField(null=True)
 
    class Meta: 
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name 

class Section(models.Model):
    section_title = models.CharField(max_length=255)
    section_rank = models.IntegerField(default=0)
    section_description = models.TextField(null=True)

    def __str__(self):
        return self.section_title

class Prompt(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prompt_category = models.CharField(max_length=255, null=True)
    prompt_title = models.CharField(max_length=45, null=True)
    prompt_text = models.TextField(null=True)
    prompt_output = models.TextField(null=True)
    prompt_language = models.CharField(max_length=255, null=True)
    prompt_warning = models.BooleanField(default=False)
    prompt_level = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.prompt_title + " (" + self.prompt_language + ")"

class Paragraph(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    paragraph_title = models.CharField(max_length=255, null=True)
    paragraph_text = models.TextField(null=True)
    prompts = models.ManyToManyField(Prompt, blank=True)

    def __str__(self):
        return self.paragraph_title
    
class Subparagraph(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    subparagraph_title = models.CharField(max_length=255, null=True, blank=True)
    subparagraph_text = models.TextField(null=True)
    prompts = models.ManyToManyField(Prompt, blank=True)

    def __str__(self):
        return self.subparagraph_title or "Untitled"

class SimplePage(models.Model):
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=False)
    slug = models.SlugField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.title
