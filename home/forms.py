from django import forms
from .models import Ride, Available

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['from1','to','date','time','Seats','card_number', 'expiry_date', 'security_code','Seats']
        widgets = {
            'date': forms.DateInput(attrs={ 'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
                  }
 
        
       