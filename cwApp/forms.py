from django import forms
from .models import Car

class CarForm (forms.ModelForm):
    class Meta:
        model= Car
        fields= '__all__'

    def clean_year(self):   #error for years
        yearData= self.cleaned_data['year']
        if yearData < 2019:
            raise forms.ValidationError ("That's not a new car")
        return yearData

    def clean_mph(self):  #errors for mph
        mphData= self.cleaned_data['mph']
        if mphData < 20:
            raise forms.ValidationError ("That's less than a truck")
        if mphData >500:
            raise forms.ValidationError ("That's impossible ('in 2019')")
        return mphData