from django import forms
from .models import ClubRep
from django.forms import ModelForm

class CreateNewUser(forms.Form):
    name = forms.CharField(label="Club Name", max_length=200)
    #check = forms.BooleanField()

CARD_TYPE = [('credit card', 'Credit Card'), ('debit card', 'Debit Card')]

#c
class RepForm(ModelForm):
    class Meta:
        model = ClubRep
        fields =  ('firstName', 'lastName', 'clubName', 'cardType', 'cardNumber', 'expiryDate')
        labels = {
            'firstName': '',
            'lastName': '',
            'clubName': 'Select Club',
            'cardType': 'Select Card Type',
            'cardNumber': '',
            'expiryDate': '',
        }


        widgets = {
            #'__all__': forms.TextInput(attrs={'class':'form-control'})
            'firstName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lastName':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            #'clubName':forms.Select(attrs={'class':'form-control','placeholder':'dsadas '}),
            'cardType':forms.Select(choices=CARD_TYPE,attrs={'class':'form-control','placeholder':'Card Type'}),
            'cardNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Card Number'}),
            'expiryDate':forms.TextInput(attrs={'class':'form-control','placeholder':'Expiry Date'}),
        }   









# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ['color']


# class ClubRep(forms.ModelForm):
#     class Meta:
#         model = ClubRep
#         fields = ('firstName', 'lastName','cardType','cardNumber', 'expiryDate')


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields[]

# class PersonCreationForm(forms.ModelForm):
#     class Meta:
#         model = ClubRep
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['cardType'].queryset = cardType.objects.none()

#         if 'country' in self.data:
#             try:
#                 country_id = int(self.data.get('country'))
#                 self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
            
#             self.fields['city'].queryset = self.instance.country.city_set.order_by('name')