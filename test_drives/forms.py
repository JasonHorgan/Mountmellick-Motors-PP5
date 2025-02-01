from django import forms
from .models import TestDrive, Stock
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TestDriveForm(forms.ModelForm):
    TIME_CHOICES = [
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('14:00', '2:00 PM'),
        ('15:00', '3:00 PM'),
        ('16:00', '4:00 PM'),
    ]
    
    
    time = forms.ChoiceField(choices=TIME_CHOICES, required=True)

    class Meta:
        model = TestDrive
        fields = ['car', 'date', 'time']  
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(TestDriveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('submit', 'Book Test Drive', css_class='btn btn-primary'))
        
       
        self.fields['car'].queryset = Stock.objects.all()  
        self.fields['car'].label_from_instance = lambda obj: f"{obj.reg_number} {obj.make} {obj.model}"  
