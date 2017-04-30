from django.contrib import admin
from django.forms import SelectMultiple

from .models import Price
from .models import Qikan
from django import forms


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        exclude = []


class PriceInline(admin.StackedInline):
    model = Price
    extra = 0
    form = PriceForm



@admin.register(Qikan)
class QikanAdmin(admin.ModelAdmin):
    list_display = ('book_name_zh', 'book_name_en', 'id')
    search_fields = ('book_name_zh', 'book_name_en')
    readonly_fields = ('book_name_zh', 'book_name_en', 'id') #都禁止修改
    fieldsets = (
        (None,{"fields":('book_name_zh', 'book_name_en')} ),
    )
    actions = None
    inlines = [PriceInline]
