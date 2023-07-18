from django.contrib import admin

from .models import Prompt, Category, Section, Paragraph, Subparagraph

# Register your models here.

class PromptInline(admin.TabularInline):
    model = Prompt
    extra = 1

class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1

class SubparagraphInline(admin.TabularInline):
    model = Subparagraph

class SectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["section_title"]}),
        (None, {"fields": ["section_description"]}),
        (None, {"fields": ["section_rank"]}),
    ] 
    inlines = [ParagraphInline]
    list_display = ["section_title", "section_rank"]

    def sortByRank(self, obj):
        return obj.section_rank
    
    sortByRank.admin_order_field =  "section_rank"

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["category_name"]}),
        (None, {"fields": ["category_information"]}),
        (None, {"fields": ["category_svg"]})
    ]
    inlines = [PromptInline]

class ParagraphPromptInline(admin.TabularInline):
    model = Paragraph.prompts.through
    extra = 1

class ParagraphAdmin(admin.ModelAdmin):
    inlines = [SubparagraphInline]

class PromptAdmin(admin.ModelAdmin):
    inlines = [ParagraphPromptInline]
    list_filter = ["category__category_name", "prompt_language"]

admin.site.register(Prompt, PromptAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Category, CategoryAdmin)