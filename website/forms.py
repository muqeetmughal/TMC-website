from distutils.command.build_scripts import first_line_re
import imp
from django import forms
from .models import Contact, Newsletter


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

        model  = Newsletter
        fields = "__all__"