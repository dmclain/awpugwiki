from django.forms import ModelForm
from .models import Page

class NewPageForm(ModelForm):
    class Meta:
        exclude = ('slug', 'user')
        model = Page

class EditPageForm(ModelForm):
    class Meta:
        exclude = ('user')
        hidden = ('title', 'slug')
        model = Page
