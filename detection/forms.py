from django import forms
from .models import XrayCTImage

class PatientImageForm(forms.ModelForm):
    # Add a new field for prediction result (you can make it a CharField or TextInput)
    prediction_result = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = XrayCTImage
        fields = ['name', 'age', 'gender', 'image', 'prediction_result']  # Add prediction_result here
