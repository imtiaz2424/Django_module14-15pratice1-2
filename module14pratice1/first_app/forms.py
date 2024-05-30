from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea)





# from .models import FirstApp

# class FirstAppForm(forms.ModelForm):
#     class Meta: 
#         model = FirstApp
#         fields = '__all__'

