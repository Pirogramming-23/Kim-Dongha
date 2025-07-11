from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'genre', 'gamdok', 'juyeon', 'year',
            'runningtime', 'score', 'text', 'text_content'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'gamdok': forms.TextInput(attrs={'class': 'form-control'}),
            'juyeon': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'runningtime': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 5}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
