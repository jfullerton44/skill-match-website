from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Student
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'sex', 'bio', 'picture')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))