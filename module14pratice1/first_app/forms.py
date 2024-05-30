from django import forms
from django.forms.widgets import NumberInput
import datetime

# from .models import FirstApp


BIRTH_YEAR_CHOICES = []
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class ContactForm(forms.Form):
    first_name = forms.CharField(initial='Your name')
    name = forms.CharField()
    message = forms.CharField(
	max_length = 25,
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    email_address = forms.EmailField( 
        required = False,
        label="Please enter your email address"
    )
    agree = forms.BooleanField(initial=True)
    notagree = forms.BooleanField()
    day = forms.DateField(initial=datetime.date.today)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    # favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    # model_choice = forms.ModelChoiceField(
    #     queryset = FirstApp.objects.all(),
    #     initial = 0
    #     )







# from .models import FirstApp

# class FirstAppForm(forms.ModelForm):
#     class Meta: 
#         model = FirstApp
#         fields = '__all__'

