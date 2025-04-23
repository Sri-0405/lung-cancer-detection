from django.shortcuts import render
from .forms import PatientImageForm
from django.core.files.storage import FileSystemStorage
import random

def home(request):
    prediction_result = None
    file_url = None

    if request.method == 'POST' and request.FILES['image']:
        form = PatientImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Process form data
            patient_name = form.cleaned_data['name']
            patient_age = form.cleaned_data['age']
            patient_gender = form.cleaned_data['gender']
            uploaded_file = request.FILES['image']
            
            # Save the uploaded image
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)

            # Fake prediction result logic (remove this when using the real model)
            prediction_result = random.choice(['Cancer Detected', 'No Cancer'])

    else:
        form = PatientImageForm()

    return render(request, 'home.html', {
        'form': form,
        'prediction_result': prediction_result,
        'file_url': file_url,
    })
