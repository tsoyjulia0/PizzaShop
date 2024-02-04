from django.shortcuts import render
from . import forms
# Create your views here.

# Form validation without Model (forms who have no models)
def form_page(request):
    form = forms.NameForm()

    if request.method == "POST":
        form = forms.NameForm(request.POST)
        if form.is_valid():
            print('Validation success')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'validformapp/form_page.html', {'form': form})
