from django import forms
from .models import Enrollment, ContactMessage

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course', 'student_name', 'student_email']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'student_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your message or security incident report...'}),
        }