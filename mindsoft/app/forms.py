from django import forms
from app.models import dept_model,auth_model
class dept_form(forms.ModelForm):
    class Meta:
        model=dept_model
        fields='__all__'


class auth_form(forms.ModelForm):
    class Meta:
        model = auth_model
        fields = '__all__'
