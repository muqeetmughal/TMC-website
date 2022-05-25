from distutils.command.build_scripts import first_line_re
import imp
from django import forms
from .models import Contact, JobApplication, Newsletter


class ContactForm(forms.ModelForm):
    # first_name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'id':'form_name'}), required=True)
    # last_name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'id':'form_name'}), required=True)
    # email= forms.EmailField(widget= forms.TextInput(attrs={'class':'form-control', 'id':'form_name'}), required=True)
    # department = forms.ModelChoiceField()
    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(forms.ModelForm):

    class Meta:

        model = Newsletter
        fields = "__all__"


class JobApplicationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'name'}), required=True)
    age = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'age'}), required=False)

    marital_status = forms.ChoiceField(
        choices=JobApplication.MaritalStatus.choices, widget=forms.Select(attrs={'class': 'form-control', 'id': 'marital_status'}), required=False)

    employer_1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'employer_1'}), required=False)
    designation_1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'designation_1'}), required=False)

    experience_1 = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'experience_1'}), required=False)

    employer_2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'employer_2'}), required=False)
    designation_2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'designation_2'}), required=False)

    experience_2 = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'experience_2'}), required=False)

    employer_3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'employer_3'}), required=False)
    designation_3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'designation_3'}), required=False)

    experience_3 = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'experience_3'}), required=False)

    cv = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'id': 'cv'}), required=False)

    audio = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'id': 'audio'}), required=False)

    class Meta:

        model = JobApplication
        fields = "__all__"
