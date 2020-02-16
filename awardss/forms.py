from django import forms
from .models import Projects

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['name', 'pub_date']
        