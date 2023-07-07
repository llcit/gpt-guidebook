from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_information = models.TextField()

    class Meta: 
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    
class Prompt(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prompt_title = models.CharField(max_length=255, null=True)
    prompt_text = models.TextField(null=True)
    prompt_output = models.TextField(null=True)
    prompt_language = models.CharField(max_length=255, null=True)
    prompt_warning = models.BooleanField(default=False)

class Section(models.Model):
    section_title = models.CharField(max_length=255)
    section_rank = models.IntegerField(default=0)
    section_description = models.TextField(null=True)

    def __str__(self):
        return self.section_title

class Paragraph(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    paragraph_title = models.CharField(max_length=255, null=True)
    paragraph_text = models.TextField(null=True)


    