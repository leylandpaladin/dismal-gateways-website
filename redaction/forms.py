from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    body = forms.Textarea()
    date_created = forms.DateField()
    author = forms.CharField()
    
