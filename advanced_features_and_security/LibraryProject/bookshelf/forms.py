# LibraryProject/bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    """
    Form definition for user input. 
    Using Django forms ensures that input is validated and sanitized, 
    mitigating XSS and SQL injection risks.
    """
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")