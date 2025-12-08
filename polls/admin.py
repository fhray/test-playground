from django.contrib import admin

from .models import Choice, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "votes", "question"]
    list_filter = ["question"]
