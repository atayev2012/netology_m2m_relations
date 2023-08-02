from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            form_data = form.cleaned_data
            if 'is_main' in form_data:
                if form_data['is_main']:
                    counter += 1

                if counter == 0:
                    raise ValidationError('Ошибка! Выберите хотя бы 1 основной тэг!')
                elif counter > 1:
                    raise ValidationError('Ошибка! Выбрано слишком много тэгов как овновной. Выберите только 1 тэг!')
                else:
                    return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopeInline,]




