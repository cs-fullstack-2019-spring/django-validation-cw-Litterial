from django import forms
from .models import Car

class CarForm (forms.ModelForm):
    class Meta:
        model= Car
        fields= '__all__'

    def findErrors(self):
         yearData= self.cleaned_data['year']
         # mphData= self.cleaned_data['mph']

         # if mphData <20:
         #     raise forms.ValidationError ("That's less than a truck")
         # if mphData >500:
         #     raise forms.ValidationError ("That's impossible (in 2019")
         if yearData >2019:
             raise forms.ValidationError ("That's not a new car")

         return yearData#,mphData
