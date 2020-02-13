from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)